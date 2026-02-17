from excalidraw_gen.core.themes.mork import Theme

def add_templates(b):
    """Full page templates (D/Page/*)"""

    # D/Page/Dashboard
    b.add_item("D/Page/Dashboard", [
        # Sidebar
        b.rectangle(0,0,240,900, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,20,"Acme", fontSize=20, extra={"fontWeight": "bold"}),
        # Topbar
        b.rectangle(240,0,1200,60, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(260,20,"Overview", fontSize=16),
        # Content
        b.text(260,90,"Dashboard", fontSize=30, extra={"fontWeight": "bold"}),
        # KPI Grid Mockup
        b.rectangle(260,150,240,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.rectangle(520,150,240,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.rectangle(780,150,240,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        # Chart Mockup
        b.rectangle(260,300,760,400, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
    ])

    # D/Page/Chat (App Shell)
    b.add_item("D/Page/Chat/AppShell", [
        # Sidebar
        b.rectangle(0,0,260,900, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,20,"+ New Chat", fontSize=14),
        # Thread Area
        b.text(600,40,"Model: GPT-4", fontSize=14, strokeColor=Theme.MUTED_FG),
        # Message
        b.ellipse(300,100,32,32, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(350,100,"How can I help you today?", fontSize=16),
        # Composer
        b.rectangle(300,750,800,100, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
    ])
