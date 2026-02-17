from excalidraw_gen.core.themes.default import Theme

def add_organisms(b):
    """Higher-order blocks and page sections (C/Block/*, C/Header/*)"""

    # --- Page Headers ---
    b.add_item("C/Header/PageTitle+Actions", [
        b.rectangle(0,0,800,80, backgroundColor=Theme.BACKGROUND, strokeColor="transparent"),
        b.text(0,10,"Customers", fontSize=30, extra={"fontWeight": "bold"}),
        b.text(0,50,"Manage your customer base and view analytics.", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.rectangle(650,10,120,40, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(650,10,"Add Customer", width=120, height=40, textAlign="center", verticalAlign="middle", strokeColor=Theme.PRIMARY_FG),
        b.rectangle(520,10,110,40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(520,10,"Export", width=110, height=40, textAlign="center", verticalAlign="middle"),
    ])

    b.add_item("C/Header/FilterBar", [
        b.rectangle(0,0,800,60, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,20,"Filter:", fontSize=14, extra={"fontWeight": "bold"}),

        b.rectangle(70,12,100,36, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(80,20,"Status", fontSize=14),

        b.rectangle(180,12,100,36, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(190,20,"Priority", fontSize=14),

        b.rectangle(290,12,100,36, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(300,20,"Assignee", fontSize=14),

        b.text(700,20,"Reset", fontSize=14, strokeColor=Theme.DESTRUCTIVE),
    ])

    # --- Marketing Blocks ---
    b.add_item("C/Block/Marketing/Hero", [
        b.rectangle(0,0,1200,400, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        # Centered headline - position from left edge for proper centering
        b.text(200,100,"Build faster with our tools", width=800, fontSize=48, textAlign="center", extra={"fontWeight": "bold"}),
        # Centered subtext
        b.text(300,180,"The open source platform for the next generation of web apps.", width=600, fontSize=20, textAlign="center", strokeColor=Theme.MUTED_FG),
        # Centered button
        b.rectangle(520,250,160,50, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(520,250,"Get Started", width=160, height=50, textAlign="center", verticalAlign="middle", strokeColor=Theme.PRIMARY_FG),
    ])

    b.add_item("C/Block/Marketing/FeatureGrid", [
        b.rectangle(0,0,280,200, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.ellipse(20,20,40,40, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(20,80,"Feature One", fontSize=20, extra={"fontWeight": "bold"}),
        b.text(20,110,"Description of the feature goes here.", fontSize=16, strokeColor=Theme.MUTED_FG),

        b.rectangle(300,0,280,200, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.ellipse(320,20,40,40, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(320,80,"Feature Two", fontSize=20, extra={"fontWeight": "bold"}),
        b.text(320,110,"Description of the feature goes here.", fontSize=16, strokeColor=Theme.MUTED_FG),

        b.rectangle(600,0,280,200, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.ellipse(620,20,40,40, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(620,80,"Feature Three", fontSize=20, extra={"fontWeight": "bold"}),
        b.text(620,110,"Description of the feature goes here.", fontSize=16, strokeColor=Theme.MUTED_FG),
    ])

    # --- CRUD Blocks ---
    b.add_item("C/Block/CRUD/List+Table", [
        # Filters Bar
        b.rectangle(0,0,800,60, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.rectangle(20,12,250,36, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(35,20,"Filter by name...", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.rectangle(290,12,120,36, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(300,20,"Status: All", width=100, fontSize=14),
        b.line(0,0, [[390,25], [395,30], [400,25]], strokeColor=Theme.MUTED_FG),

        # Table
        b.rectangle(0,80,800,300, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.line(0,120, [[0,0], [800,0]], strokeColor=Theme.BORDER),
        b.text(20,95, "Name", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(300,95, "Status", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(500,95, "Role", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(700,95, "Actions", fontSize=14, extra={"fontWeight": "bold"}),

        # Row 1
        b.text(20,140, "Alice Smith", fontSize=14),
        b.rectangle(300,135,60,24, backgroundColor=Theme.SUCCESS_BG, strokeColor=Theme.SUCCESS_BORDER, fillStyle="solid"),
        b.text(300,135, "Active", width=60, height=24, textAlign="center", verticalAlign="middle", fontSize=12, strokeColor=Theme.SUCCESS_TEXT),
        b.text(500,140, "Admin", fontSize=14),
        b.text(710,135, "...", fontSize=20, extra={"fontWeight": "bold"}),
        b.line(0,170, [[0,0], [800,0]], strokeColor=Theme.BORDER),

        # Row 2
        b.text(20,190, "Bob Jones", fontSize=14),
        b.rectangle(300,185,60,24, backgroundColor=Theme.GRAY_100, strokeColor=Theme.GRAY_300, fillStyle="solid"),
        b.text(300,185, "Offline", width=60, height=24, textAlign="center", verticalAlign="middle", fontSize=12, strokeColor=Theme.GRAY_700),
        b.text(500,190, "User", fontSize=14),
        b.text(710,185, "...", fontSize=20, extra={"fontWeight": "bold"}),

        # Pagination Footer
        b.line(0,320, [[0,0], [800,0]], strokeColor=Theme.BORDER),
        b.text(20,345, "Page 1 of 10", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.rectangle(650,335,60,32, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(650,335,"Prev", width=60, height=32, textAlign="center", verticalAlign="middle", fontSize=12),
        b.rectangle(720,335,60,32, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(720,335,"Next", width=60, height=32, textAlign="center", verticalAlign="middle", fontSize=12),
    ])

    b.add_item("C/Block/CRUD/SettingsNav", [
        b.rectangle(0,0,240,400, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,20,"Settings", fontSize=18, extra={"fontWeight": "bold"}),
        b.text(20,60,"General", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(20,95,"Security", fontSize=14),
        b.text(20,130,"Team", fontSize=14),
        b.text(20,165,"Billing", fontSize=14),
        b.text(20,200,"Notifications", fontSize=14),
    ])

    # --- Dashboard Blocks ---
    b.add_item("C/Block/Dashboard/KPIGrid", [
        # Card 1
        b.rectangle(0,0,240,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,20,"Total Revenue", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(20,50,"$45,231.89", fontSize=24, extra={"fontWeight": "bold"}),
        b.text(20,90,"+20.1% month over month", fontSize=12, strokeColor=Theme.MUTED_FG),
        # Card 2
        b.rectangle(260,0,240,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(280,20,"Subscriptions", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(280,50,"+2350", fontSize=24, extra={"fontWeight": "bold"}),
        b.text(280,90,"+180.1% month over month", fontSize=12, strokeColor=Theme.MUTED_FG),
        # Card 3
        b.rectangle(520,0,240,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(540,20,"Active Now", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(540,50,"+573", fontSize=24, extra={"fontWeight": "bold"}),
        b.text(540,90,"+201 since last hour", fontSize=12, strokeColor=Theme.MUTED_FG),
    ])

    # --- Search ---
    b.add_item("C/Block/SearchResults/List", [
        b.text(0,0,"Results for \"design system\"", fontSize=18, extra={"fontWeight": "bold"}),
        # Result 1
        b.text(0,40,"Design System Documentation", fontSize=16, strokeColor=Theme.INFO, extra={"textDecoration": "underline"}),
        b.text(0,65,"The official documentation for our design system including colors, typography...", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.text(0,90,"https://acme.com/docs/design-system", fontSize=12, strokeColor=Theme.SUCCESS),
        # Result 2
        b.text(0,130,"Component Library - Figma", fontSize=16, strokeColor=Theme.INFO, extra={"textDecoration": "underline"}),
        b.text(0,155,"Figma community file for the component library...", fontSize=14, strokeColor=Theme.MUTED_FG),
    ])

    # Additional high-level patterns
    b.add_item("C/Block/AlertDialog", [
        b.rectangle(0,0,450,250, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(30,30,"Are you absolutely sure?", fontSize=22, extra={"fontWeight": "bold"}),
        b.text(30,75,"This action cannot be undone. This will permanently delete your account and remove your data from our servers.", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.rectangle(240,190,90,40, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(240,190,"Cancel", width=90, height=40, textAlign="center", verticalAlign="middle"),
        b.rectangle(340,190,90,40, backgroundColor=Theme.DESTRUCTIVE, fillStyle="solid"),
        b.text(340,190,"Continue", width=90, height=40, textAlign="center", verticalAlign="middle", strokeColor=Theme.DESTRUCTIVE_FG),
    ])
    b.add_item("C/Block/AspectRatio", [
        b.rectangle(0,0,400,225, backgroundColor=Theme.MUTED, fillStyle="solid", strokeColor=Theme.BORDER),
        b.text(0,0,"16:9 Container", width=400, height=225, textAlign="center", verticalAlign="middle", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.text(10,195,"400 × 225", fontSize=12, strokeColor=Theme.MUTED_FG),
    ])
    b.add_item("C/Block/Skeleton/Complex", [
        b.rectangle(0,0,400,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.ellipse(20,20,80,80, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.rectangle(120,20,260,20, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.rectangle(120,50,200,20, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.rectangle(120,80,140,20, backgroundColor=Theme.MUTED, fillStyle="solid"),
    ])
