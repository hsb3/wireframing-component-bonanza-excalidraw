from excalidraw_gen.core.themes.mork import Theme

def add_shells(b):
    """App Shell Layouts (C/Shell/*)"""

    # Standard Dashboard Shell (3-Pane)
    b.add_item("C/Shell/App/3Pane", [
        # Wrapper
        b.rectangle(0,0,1200,800, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        # Sidebar
        b.line(0,0, [[250,0], [250,800]], strokeColor=Theme.BORDER),
        b.text(20,20,"App", fontSize=20, extra={"fontWeight": "bold"}),
        # List View
        b.line(0,0, [[550,0], [550,800]], strokeColor=Theme.BORDER),
        b.text(270,20,"List", fontSize=16, extra={"fontWeight": "bold"}),
        # Detail View
        b.text(570,20,"Detail", fontSize=16, extra={"fontWeight": "bold"}),
    ])

    # Browser Window Frame
    b.add_item("C/Shell/BrowserWindow", [
        b.rectangle(0,0,1024,768, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.line(0,40, [[0,0], [1024,0]], strokeColor=Theme.BORDER), # Url bar divider
        # Traffic lights
        b.ellipse(15,12,12,12, backgroundColor=Theme.DESTRUCTIVE, fillStyle="solid", strokeColor="transparent"),
        b.ellipse(35,12,12,12, backgroundColor=Theme.WARNING, fillStyle="solid", strokeColor="transparent"),
        b.ellipse(55,12,12,12, backgroundColor=Theme.SUCCESS_BRIGHT, fillStyle="solid", strokeColor="transparent"),
        # Url bar
        b.rectangle(90,8,600,24, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(100,10,"https://acme.com", fontSize=12, strokeColor=Theme.MUTED_FG),
    ])

    # Split View Layout
    b.add_item("C/Shell/SplitView", [
        b.rectangle(0,0,1200,800, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.line(0,0, [[600,0], [600,800]], strokeColor=Theme.BORDER),
        b.text(20,20,"Editor", fontSize=20, extra={"fontWeight": "bold"}),
        b.text(620,20,"Preview", fontSize=20, extra={"fontWeight": "bold"}),
    ])

    # Right Inspector Panel
    b.add_item("C/Shell/RightInspector", [
         b.rectangle(0,0,1200,800, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
         b.line(0,0, [[900,0], [900,800]], strokeColor=Theme.BORDER),
         b.text(20,20,"Main Content", fontSize=20, extra={"fontWeight": "bold"}),
         b.text(920,20,"Properties", fontSize=16, extra={"fontWeight": "bold"}),
    ])

    # Mobile Bottom Nav Shell
    b.add_item("C/Shell/Mobile/BottomNav", [
        b.rectangle(0,0,390,60, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        # Items
        b.text(30,10,"Home", fontSize=12, textAlign="center"),
        b.text(130,10,"Search", fontSize=12, textAlign="center", strokeColor=Theme.MUTED_FG),
        b.text(230,10,"Orders", fontSize=12, textAlign="center", strokeColor=Theme.MUTED_FG),
        b.text(330,10,"Profile", fontSize=12, textAlign="center", strokeColor=Theme.MUTED_FG),
    ])

    # Mobile Drawer Nav
    b.add_item("C/Block/Mobile/DrawerNav", [
        b.rectangle(0,0,300,844, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,40,"Menu", fontSize=24, extra={"fontWeight": "bold"}),
        b.line(0,80, [[0,0], [300,0]], strokeColor=Theme.BORDER),
        b.text(20,100,"Home", fontSize=16),
        b.text(20,140,"Shop", fontSize=16),
        b.text(20,180,"About", fontSize=16),
    ])
