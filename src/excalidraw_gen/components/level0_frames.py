from excalidraw_gen.core.themes.mork import Theme

def add_frames(b):
    """Device Frames & Layout Primitives"""

    # --- Device Frames (scaled to 1/5 for proportionate wireframe sizing) ---
    # Desktop (1440x900 → 288x180)
    b.add_item("Frame: Desktop (1440x900)", [
        b.rectangle(0, 0, 288, 180, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(10, -25, "Desktop 1440px", fontSize=12, strokeColor=Theme.MUTED_FG)
    ])

    # Tablet (768x1024 → 154x205)
    b.add_item("Frame: Tablet (768x1024)", [
        b.rectangle(0, 0, 154, 205, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(10, -25, "Tablet 768px", fontSize=12, strokeColor=Theme.MUTED_FG)
    ])

    # Mobile (375x812 → 75x162)
    b.add_item("Frame: Mobile (375x812)", [
        b.rectangle(0, 0, 75, 162, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(10, -25, "Mobile 375px", fontSize=12, strokeColor=Theme.MUTED_FG),
        # notch mock (scaled proportionally)
        b.rectangle(17, 0, 40, 6, backgroundColor=Theme.PRIMARY, fillStyle="solid")
    ])

    # --- Layout Primitives ---
    # Divider
    b.add_item("Layout: Divider Horizontal", [
        b.line(0,0, [[0,0], [300,0]], strokeColor=Theme.BORDER)
    ])
    b.add_item("Layout: Divider Vertical", [
        b.line(0,0, [[0,0], [0,300]], strokeColor=Theme.BORDER)
    ])
    
    # 12 Col Grid Overlay
    col_w = 60
    gap = 20
    grid_els = []
    for i in range(12):
        x = i * (col_w + gap)
        grid_els.append(b.rectangle(x, 0, col_w, 200, backgroundColor=Theme.INFO_SUBTLE_BG, fillStyle="solid", strokeColor="transparent", opacity=30))
    b.add_item("Layout: Grid 12-col", grid_els)
    
    # Scroll Area
    b.add_item("Layout: Scroll Area", [
        b.rectangle(0,0,300, 400, backgroundColor=Theme.GRAY_50, strokeColor=Theme.BORDER, strokeStyle="dashed"),
        b.rectangle(290, 50, 6, 100, backgroundColor=Theme.MUTED_FG, fillStyle="solid")
    ])
