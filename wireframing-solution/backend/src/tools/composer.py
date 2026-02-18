"""
Wireframe composition engine
Loads components from library and composes them into .excalidraw files
"""
import json
from pathlib import Path
from typing import Optional


class WireframeComposer:
    """Compose wireframes from component library"""

    def __init__(self, component_registry: dict):
        self.registry = component_registry
        self.library_cache = {}

    def compose(
        self,
        name: str,
        theme: str,
        components: list[dict],
        canvas_size: Optional[dict] = None
    ) -> dict:
        """
        Compose wireframe from components.

        Args:
            name: Output filename (without extension)
            theme: Theme (mork, abc123-dark, bronzer)
            components: [{"component_id": "...", "x": 100, "y": 200, "customizations": {...}}]
            canvas_size: Optional {"width": 1200, "height": 800}

        Returns:
            {"file": Path, "element_count": int, "dimensions": {...}}
        """
        elements = []
        element_id_counter = 1000

        for comp_spec in components:
            comp_id = comp_spec.get('component_id')
            offset_x = comp_spec.get('x', 0)
            offset_y = comp_spec.get('y', 0)
            customizations = comp_spec.get('customizations', {})

            # Get component from registry
            component = self._get_component_by_id(comp_id)
            if not component:
                continue

            # Load component elements from library
            comp_elements = self._load_component_elements(component)

            # Translate and add to scene
            for element in comp_elements:
                new_element = element.copy()

                # Translate position
                new_element['x'] = element.get('x', 0) + offset_x
                new_element['y'] = element.get('y', 0) + offset_y

                # Generate new ID
                new_element['id'] = f"element-{element_id_counter}"
                element_id_counter += 1

                # Apply customizations (text replacement)
                if element.get('type') == 'text' and 'text' in customizations:
                    new_element['text'] = customizations['text']

                elements.append(new_element)

        # Create Excalidraw document
        canvas_size = canvas_size or {'width': 1200, 'height': 800}

        excalidraw_doc = {
            'type': 'excalidraw',
            'version': 2,
            'source': 'wireframe-agent',
            'elements': elements,
            'appState': {
                'viewBackgroundColor': '#ffffff' if theme == 'mork' else '#161616',
                'currentItemStrokeColor': '#000000',
                'currentItemBackgroundColor': 'transparent',
                'gridSize': None
            },
            'files': {}
        }

        # Save file
        output_dir = Path(__file__).parent.parent.parent.parent.parent / 'wireframes'
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / f"{name}.excalidraw"
        with open(output_file, 'w') as f:
            json.dump(excalidraw_doc, f, indent=2)

        # Calculate actual dimensions
        if elements:
            xs = [el.get('x', 0) for el in elements]
            ys = [el.get('y', 0) for el in elements]
            widths = [el.get('x', 0) + el.get('width', 0) for el in elements if 'width' in el]
            heights = [el.get('y', 0) + el.get('height', 0) for el in elements if 'height' in el]

            actual_dims = {
                'width': int(max(widths) - min(xs)) if widths and xs else 100,
                'height': int(max(heights) - min(ys)) if heights and ys else 100
            }
        else:
            actual_dims = {'width': 0, 'height': 0}

        return {
            'file': output_file,
            'element_count': len(elements),
            'dimensions': actual_dims
        }

    def _get_component_by_id(self, component_id: str) -> Optional[dict]:
        """Find component in registry by ID"""
        for comp in self.registry['components']:
            if comp['id'] == component_id:
                return comp
        return None

    def _load_component_elements(self, component: dict) -> list[dict]:
        """Load Excalidraw elements for a component from library file"""
        library_file = Path(__file__).parent.parent.parent.parent.parent / component['library_file']

        # Cache library files
        lib_key = str(library_file)
        if lib_key not in self.library_cache:
            with open(library_file) as f:
                self.library_cache[lib_key] = json.load(f)

        library = self.library_cache[lib_key]

        # Get specific library item by index
        library_items = library.get('libraryItems', [])
        idx = component['library_index']

        if idx < len(library_items):
            return library_items[idx].get('elements', [])

        return []
