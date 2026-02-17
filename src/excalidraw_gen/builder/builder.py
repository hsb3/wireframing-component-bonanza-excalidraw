
import random
import time
from excalidraw_gen.core.themes.mork import Theme as DefaultTheme

def generate_id():
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=20))

def get_timestamp():
    return int(time.time() * 1000)

def estimate_text_dimensions(content, font_size=20, font_family=1, padding=4):
    """
    Estimate the width and height needed for text content.

    Args:
        content: Text content (supports newlines)
        font_size: Font size in pixels
        font_family: 1=Virgil (hand-drawn), 2=Helvetica, 3=Cascadia (code)
        padding: Extra padding in pixels (added to both width and height)

    Returns:
        (width, height) tuple
    """
    lines = content.split('\n')

    # Font-specific character width multipliers (approximate)
    # Virgil (hand-drawn) is wider and more irregular
    char_width_multipliers = {
        1: 0.65,  # Virgil (hand-drawn) - wider characters
        2: 0.55,  # Helvetica (sans-serif) - more compact
        3: 0.6,   # Cascadia (monospace) - fixed width
    }

    multiplier = char_width_multipliers.get(font_family, 0.6)

    # Calculate width based on longest line
    max_line_length = len(max(lines, key=len)) if lines else 0
    estimated_width = max_line_length * font_size * multiplier + padding * 2

    # Calculate height based on number of lines
    line_height = font_size * 1.2  # Standard line-height ratio
    estimated_height = len(lines) * line_height + padding * 2

    return (int(estimated_width), int(estimated_height))

class ExcalidrawBuilder:
    def __init__(self, theme=None):
        """
        Initialize ExcalidrawBuilder.

        Args:
            theme: Theme class to use (defaults to DefaultTheme)
        """
        self.library_items = []
        self.theme = theme or DefaultTheme

    def create_base_element(self, type, x, y, width, height, **kwargs):
        element = {
            "id": generate_id(),
            "type": type,
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "angle": 0,
            "strokeColor": self.theme.FOREGROUND,
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": self.theme.STROKE_WIDTH,
            "strokeStyle": self.theme.STROKE_STYLE,
            "roughness": self.theme.ROUGHNESS,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": None,
            "seed": random.randint(1, 100000000),
            "version": 1,
            "versionNonce": 0,
            "isDeleted": False,
            "boundElements": None,
            "updated": get_timestamp(),
            "link": None,
            "locked": False,
        }

        # Apply default roundness based on type (if not in kwargs)
        if "roundness" not in kwargs:
            if type == "rectangle":
                # Use theme roundness if available, otherwise default to 3
                roundness_type = getattr(self.theme, 'ROUNDNESS_TYPE', 3)
                # Type 1 = sharp corners in carbon, but set to null for truly boxy
                if roundness_type == 1:
                    element["roundness"] = None  # No rounding for carbon
                else:
                    element["roundness"] = {"type": roundness_type}
            elif type == "line" or type == "arrow":
                element["roundness"] = {"type": 2}  # Slight curve

        element.update(kwargs)
        return element

    def rectangle(self, x, y, width, height, **kwargs):
        return self.create_base_element("rectangle", x, y, width, height, **kwargs)

    def ellipse(self, x, y, width, height, **kwargs):
        return self.create_base_element("ellipse", x, y, width, height, **kwargs)
        
    def line(self, x, y, points, **kwargs):
        min_x = min(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_x = max(p[0] for p in points)
        max_y = max(p[1] for p in points)
        w = max_x - min_x
        h = max_y - min_y
        return self.create_base_element("line", x, y, w, h, points=points, **kwargs)
    
    def arrow(self, x, y, points, **kwargs):
        el = self.line(x, y, points, **kwargs)
        el["type"] = "arrow"
        return el

    def text(self, x, y, content, **kwargs):
        # Extract font properties to estimate dimensions
        font_size = kwargs.get("fontSize", 20)
        font_family = kwargs.get("fontFamily", self.theme.FONT_FAMILY)

        # Estimate dimensions if not provided
        estimated_w, estimated_h = estimate_text_dimensions(
            content,
            font_size=font_size,
            font_family=font_family
        )

        defaults = {
            "text": content,
            "fontSize": font_size,
            "fontFamily": font_family,
            "textAlign": "left",
            "verticalAlign": "top",
            "baseline": int(font_size * 0.9),  # Baseline scales with font size
            "containerId": None,
            "originalText": content,
        }

        # Allow manual override of width/height
        w = kwargs.pop("width", estimated_w)
        h = kwargs.pop("height", estimated_h)
        final_props = {**defaults, **kwargs}

        return self.create_base_element("text", x, y, w, h, **final_props)

    def add_item(self, name, elements):
        group_id = generate_id()
        for el in elements:
            el["groupIds"].append(group_id)
            
        self.library_items.append({
            "id": generate_id(),
            "status": "published",
            "created": get_timestamp(),
            "name": name,
            "elements": elements
        })

    def save(self, filename="library.excalidrawlib"):
        import json
        data = {
            "type": "excalidrawlib",
            "version": 2,
            "source": "https://excalidraw.com",
            "libraryItems": self.library_items
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Generated {len(self.library_items)} items to {filename}")

    def save_preview(self, filename="library-preview.excalidraw", columns=3, spacing=50):
        """
        Export all library items as an organized .excalidraw document.

        Args:
            filename: Output filename
            columns: Number of columns in the grid layout
            spacing: Spacing between items (in pixels)
        """
        import json

        all_elements = []
        current_x = spacing
        current_y = spacing
        max_height_in_row = 0
        column_count = 0
        current_section = None

        for item in self.library_items:
            item_name = item["name"]

            # Detect section changes (e.g., "A/", "B/", "C/", etc.)
            section_prefix = item_name.split("/")[0] if "/" in item_name else item_name.split(":")[0]

            # Add section header when section changes
            if section_prefix != current_section:
                # Move to new row for section header
                if column_count > 0:
                    current_y += max_height_in_row + spacing * 2
                    current_x = spacing
                    column_count = 0
                    max_height_in_row = 0

                # Create section header
                section_header = self.text(
                    current_x,
                    current_y,
                    section_prefix,
                    fontSize=24,
                    strokeColor=self.theme.PRIMARY,
                    extra={"fontWeight": "bold"}
                )
                all_elements.append(section_header)

                # Underline
                underline = self.line(
                    current_x,
                    current_y + 30,
                    [[0, 0], [200, 0]],
                    strokeColor=self.theme.PRIMARY,
                    strokeWidth=2
                )
                all_elements.append(underline)

                current_y += 60
                current_section = section_prefix

            # Calculate bounds of the library item
            item_elements = item["elements"]
            if not item_elements:
                continue

            min_x = min(el["x"] for el in item_elements)
            min_y = min(el["y"] for el in item_elements)
            max_x = max(el["x"] + el.get("width", 0) for el in item_elements)
            max_y = max(el["y"] + el.get("height", 0) for el in item_elements)

            item_width = max_x - min_x
            item_height = max_y - min_y

            # Add label above the component
            label = self.text(
                current_x,
                current_y,
                item_name,
                fontSize=12,
                strokeColor=self.theme.MUTED_FG
            )
            all_elements.append(label)

            # Offset elements to current position
            for el in item_elements:
                el_copy = el.copy()
                el_copy["x"] = el["x"] - min_x + current_x
                el_copy["y"] = el["y"] - min_y + current_y + 25  # 25px below label
                el_copy["id"] = generate_id()  # Generate new ID
                el_copy["groupIds"] = []  # Clear group IDs
                all_elements.append(el_copy)

            # Add light border around component
            border = self.rectangle(
                current_x - 10,
                current_y - 5,
                max(item_width + 20, 200),
                item_height + 40,
                backgroundColor="transparent",
                strokeColor=self.theme.BORDER,
                strokeStyle="dashed",
                opacity=50
            )
            all_elements.append(border)

            # Update position for next item
            max_height_in_row = max(max_height_in_row, item_height + 50)
            column_count += 1

            if column_count >= columns:
                # Move to next row
                current_y += max_height_in_row + spacing
                current_x = spacing
                column_count = 0
                max_height_in_row = 0
            else:
                # Move to next column
                current_x += max(item_width + 40, 300)

        # Create the Excalidraw document
        data = {
            "type": "excalidraw",
            "version": 2,
            "source": "https://excalidraw.com",
            "elements": all_elements,
            "appState": {
                "gridSize": None,
                "viewBackgroundColor": "#ffffff"
            },
            "files": {}
        }

        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

        print(f"Generated preview document with {len(self.library_items)} components to {filename}")
