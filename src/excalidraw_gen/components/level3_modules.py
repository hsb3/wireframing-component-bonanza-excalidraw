from excalidraw_gen.core.themes.mork import Theme

def add_modules(b):
    """Composite Components (Cards, Navs, Lists)"""
    
    # Avatar Group
    av_size = 40
    b.add_item("Module: Avatar Group", [
        b.ellipse(0, 0, av_size, av_size, backgroundColor=Theme.MUTED, strokeColor=Theme.BACKGROUND, strokeWidth=2, fillStyle="solid"),
        b.ellipse(25, 0, av_size, av_size, backgroundColor=Theme.MUTED, strokeColor=Theme.BACKGROUND, strokeWidth=2, fillStyle="solid"),
        b.ellipse(50, 0, av_size, av_size, backgroundColor=Theme.MUTED, strokeColor=Theme.BACKGROUND, strokeWidth=2, fillStyle="solid"),
        b.text(50, 0, "+3", width=av_size, height=av_size, strokeColor=Theme.MUTED_FG, textAlign="center", verticalAlign="middle")
    ])
    
    # Menu Item
    b.add_item("Module: Menu Item", [
        b.rectangle(0,0,200,40, backgroundColor=Theme.BACKGROUND, strokeColor="transparent"),
        b.text(10,10,"Profile", fontSize=16),
        b.text(140,10,"⇧⌘P", fontSize=12, strokeColor=Theme.MUTED_FG)
    ])
    
    # Card
    b.add_item("Module: Card (Simple)", [
        b.rectangle(0,0,300,180, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,20,"Notification Settings", fontSize=18, extra={"fontWeight": "bold"}),
        b.text(20,45,"Choose what you want to be notified about.", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.line(0,0, [[0,120], [300,120]], strokeColor=Theme.BORDER), # footer div
        b.text(20,135,"2 unread messages", fontSize=14),
    ])
    
    # Accordion
    b.add_item("Module: Accordion", [
        b.line(0,0, [[0,0], [300,0]], strokeColor=Theme.BORDER),
        b.text(0,10,"Is it accessible?", fontSize=16, extra={"fontWeight": "bold"}),
        b.line(0,0, [[280,15], [285,20], [290,15]], strokeColor=Theme. FOREGROUND), # chevron
        b.line(0,0, [[0,40], [300,40]], strokeColor=Theme.BORDER),
        b.text(0,50,"Yes. It adheres to the WAI-ARIA design pattern.", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.line(0,0, [[0,100], [300,100]], strokeColor=Theme.BORDER),
    ])
    
    # Tabs
    b.add_item("Module: Tabs", [
        b.rectangle(0,0,320,40, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.rectangle(4,4,154,32, backgroundColor=Theme.BACKGROUND, fillStyle="solid"),
        b.text(0,0,"Account", width=160, height=40, textAlign="center", verticalAlign="middle", strokeColor=Theme.FOREGROUND, fontSize=16),
        b.text(160,0,"Password", width=160, height=40, textAlign="center", verticalAlign="middle", strokeColor=Theme.MUTED_FG, fontSize=16)
    ])
    
    # Breadcrumb
    b.add_item("Module: Breadcrumb", [
        b.text(0,0,"Home", strokeColor=Theme.MUTED_FG, fontSize=16),
        b.text(55,0,"/", strokeColor=Theme.MUTED_FG, fontSize=16),
        b.text(75,0,"Projects", strokeColor=Theme.MUTED_FG, fontSize=16),
        b.text(145,0,"/", strokeColor=Theme.MUTED_FG, fontSize=16),
        b.text(165,0,"Settings", strokeColor=Theme.FOREGROUND, fontSize=16),
    ])
    
    # Pagination
    b.add_item("Module: Pagination", [
        b.text(0,0,"Prev", strokeColor=Theme.FOREGROUND, fontSize=16),
        b.rectangle(50, -5, 30, 30, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(50, -5, "1", width=30, height=30, textAlign="center", verticalAlign="middle"),
        b.text(90, 0, "2", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.text(120, 0, "...", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.text(150, 0, "Next", strokeColor=Theme.FOREGROUND, fontSize=16),
    ])

    # Navigation
    b.add_item("Nav: Sidebar (Collapsed)", [
       b.rectangle(0,0,60,500, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
       b.rectangle(15,20,30,30, backgroundColor=Theme.PRIMARY, fillStyle="solid"), # Logo
       b.rectangle(15,80,30,30, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
       b.rectangle(15,120,30,30, strokeColor="transparent"), # Icon Placeholder
       b.rectangle(15,160,30,30, strokeColor="transparent"), # Icon Placeholder
       b.ellipse(15,450,30,30, backgroundColor=Theme.MUTED, fillStyle="solid") # Avatar
    ])
    
    # Data Display
    b.add_item("Data: KPI Row", [
        b.rectangle(0,0,180,100, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(15,15,"Users", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(15,45,"1,234", fontSize=24, extra={"fontWeight": "bold"}),
        b.text(15,75,"+12%", fontSize=12, strokeColor=Theme.MUTED_FG),
        
        b.rectangle(200,0,180,100, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(215,15,"Revenue", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(215,45,"$12k", fontSize=24, extra={"fontWeight": "bold"}),
        b.text(215,75,"+5%", fontSize=12, strokeColor=Theme.MUTED_FG),
        
        b.rectangle(400,0,180,100, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(415,15,"Bounce", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(415,45,"42%", fontSize=24, extra={"fontWeight": "bold"}),
        b.text(415,75,"-2%", fontSize=12, strokeColor=Theme.MUTED_FG),
    ])

    b.add_item("Data: Chart (Pie)", [
        b.ellipse(0,0,150,150, strokeColor=Theme.BORDER),
        b.line(75,75, [[0,0], [75, -75]], strokeColor=Theme.BORDER), # vertical up
        b.line(75,75, [[0,0], [75, 40]], strokeColor=Theme.BORDER), # right down
        b.line(75,75, [[0,0], [-70, 40]], strokeColor=Theme.BORDER), # left down
        b.text(170, 20, "Category A", fontSize=14),
        b.text(170, 50, "Category B", fontSize=14),
        b.text(170, 80, "Category C", fontSize=14),
    ])

    # Overlays
    b.add_item("Overlay: Modal (Confirm)", [
        b.rectangle(0,0,400,200, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(20,20,"Delete Account", fontSize=20, extra={"fontWeight": "bold"}),
        b.text(20,60,"Are you sure? This action cannot be undone.", width=360, fontSize=16, strokeColor=Theme.MUTED_FG),
        b.rectangle(200,140,80,40, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(200,140,"Cancel", width=80, height=40, textAlign="center", verticalAlign="middle"),
        b.rectangle(300,140,80,40, backgroundColor=Theme.DESTRUCTIVE, fillStyle="solid"),
        b.text(300,140,"Delete", width=80, height=40, textAlign="center", verticalAlign="middle", strokeColor=Theme.DESTRUCTIVE_FG),
    ])

    b.add_item("Overlay: Drawer (Right)", [
        b.rectangle(0,0,300,800, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(20,20,"Edit Profile", fontSize=20, extra={"fontWeight": "bold"}),
        b.line(0,0, [[0,60], [300,60]], strokeColor=Theme.BORDER),
        b.text(20, 80, "Name", fontSize=14),
        b.rectangle(20, 105, 260, 40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.rectangle(20, 740, 260, 40, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(20, 740, "Save Changes", width=260, height=40, textAlign="center", verticalAlign="middle", strokeColor=Theme.PRIMARY_FG),
    ])

    # Additional molecules from generate_library
    b.add_item("B/Nav/Tabs/Line", [
        b.text(0,0, "Overview", fontSize=16, strokeColor=Theme.FOREGROUND),
        b.line(0,25, [[0,0], [70,0]], strokeColor=Theme.FOREGROUND, strokeWidth=2),
        b.text(90,0, "Analytics", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.text(180,0, "Reports", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.text(260,0, "Settings", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.line(0,26, [[0,0], [350,0]], strokeColor=Theme.BORDER),
    ])
    b.add_item("B/Nav/Menu/Vertical", [
        b.rectangle(0,0,200,160, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(10,10, "Account Settings", fontSize=14),
        b.text(10,40, "Billing", fontSize=14),
        b.text(10,70, "Notifications", fontSize=14),
        b.line(0,100, [[0,0], [200,0]], strokeColor=Theme.BORDER),
        b.text(10,110, "Logout", fontSize=14, strokeColor=Theme.DESTRUCTIVE),
    ])
    b.add_item("B/Nav/WizardSteps", [
        b.ellipse(0,0,30,30, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(0,0,"1", width=30, height=30, textAlign="center", verticalAlign="middle", strokeColor=Theme.PRIMARY_FG),
        b.text(40,5,"Account", fontSize=16, extra={"fontWeight": "bold"}),
        b.line(110,15, [[0,0], [40,0]], strokeColor=Theme.PRIMARY),
        b.ellipse(160,0,30,30, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(160,0,"2", width=30, height=30, textAlign="center", verticalAlign="middle", strokeColor=Theme.MUTED_FG),
        b.text(200,5,"Profile", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.line(260,15, [[0,0], [40,0]], strokeColor=Theme.BORDER),
        b.ellipse(310,0,30,30, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(310,0,"3", width=30, height=30, textAlign="center", verticalAlign="middle", strokeColor=Theme.MUTED_FG),
        b.text(350,5,"Review", fontSize=16, strokeColor=Theme.MUTED_FG),
    ])

    # Additional cards
    b.add_item("B/Card/Metric/Trend", [
        b.rectangle(0,0,240,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,20,"Active Users", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(20,50,"1,234", fontSize=28, extra={"fontWeight": "bold"}),
        b.line(140,50, [[0,0], [20,-10], [40,-5], [60,-20], [80,-15]], strokeColor=Theme.SUCCESS, strokeWidth=2)
    ])
    b.add_item("B/Card/ListItem", [
        b.rectangle(0,0,400,80, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.ellipse(20,20,40,40, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.text(70,20,"Project Alpha", fontSize=16, extra={"fontWeight": "bold"}),
        b.text(70,45,"Last updated 2 hours ago", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.text(350,30,"...", fontSize=20, extra={"fontWeight": "bold"}),
    ])
    b.add_item("B/Card/Pricing", [
        b.rectangle(0,0,280,400, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,30,"Pro Plan", fontSize=20, extra={"fontWeight": "bold"}),
        b.text(20,60,"$29/mo", fontSize=30, extra={"fontWeight": "bold"}),
        b.text(20,100,"Everything in Basic, plus:", fontSize=14),
        b.text(20,130,"• Unlimited projects", fontSize=14),
        b.text(20,160,"• Priority support", fontSize=14),
        b.rectangle(20,340,240,40, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(20,340,"Subscribe", width=240, height=40, textAlign="center", verticalAlign="middle", strokeColor=Theme.PRIMARY_FG),
    ])

    # Charts
    b.add_item("B/Chart/Placeholder/Line", [
        b.rectangle(0,0,300,150, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.line(20,130, [[0,0], [40,-30], [80,-20], [120,-80], [160,-60], [200,-100], [260,-90]], strokeColor=Theme.PRIMARY, strokeWidth=2)
    ])
    b.add_item("B/Chart/Placeholder/Bar", [
        b.rectangle(0,0,300,150, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.rectangle(20,50,30,80, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.rectangle(70,20,30,110, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.rectangle(120,80,30,50, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.rectangle(170,40,30,90, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.rectangle(220,60,30,70, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
    ])
    b.add_item("B/Chart/Placeholder/Pie", [
        b.rectangle(0,0,200,200, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.ellipse(50,50,100,100, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.PRIMARY, strokeWidth=2),
        b.line(100,100, [[0,0], [0,-50]], strokeColor=Theme.PRIMARY),
        b.line(100,100, [[0,0], [40,30]], strokeColor=Theme.PRIMARY),
        b.line(100,100, [[0,0], [-40,20]], strokeColor=Theme.PRIMARY),
    ])

    # Additional overlays
    b.add_item("B/Overlay/Toast", [
        b.rectangle(0,0,300,60, backgroundColor=Theme.FOREGROUND, fillStyle="solid"),
        b.text(20,20,"Changes saved successfully.", fontSize=14, strokeColor=Theme.BACKGROUND),
        b.text(240,20,"Undo", fontSize=14, strokeColor=Theme.BACKGROUND, extra={"fontWeight": "bold"}),
    ])
    b.add_item("B/Overlay/ToastStack", [
        b.rectangle(0,0,320,60, backgroundColor=Theme.FOREGROUND, fillStyle="solid"),
        b.text(20,20,"File uploaded successfully", fontSize=14, strokeColor=Theme.BACKGROUND),
        b.rectangle(0,70,320,60, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(20,90,"Connection lost. Retrying...", fontSize=14, strokeColor=Theme.FOREGROUND),
    ])
    b.add_item("B/Overlay/Modal/Complex", [
        b.rectangle(0,0,600,400, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(30,30,"Edit Profile", fontSize=24, extra={"fontWeight": "bold"}),
        b.line(0,70, [[0,0], [600,0]], strokeColor=Theme.BORDER),
        b.text(30,85,"General", fontSize=14, strokeColor=Theme.PRIMARY),
        b.line(30,105, [[0,0], [50,0]], strokeColor=Theme.PRIMARY, strokeWidth=2),
        b.text(100,85,"Password", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.text(180,85,"Notifications", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.text(30,130,"DisplayName", fontSize=14),
        b.rectangle(30,155,540,40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(40,165,"John Doe", fontSize=16),
        b.text(30,215,"Bio", fontSize=14),
        b.rectangle(30,240,540,80, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(40,250,"Software Engineer at Acme Inc.", fontSize=16),
        b.line(0,340, [[0,0], [600,0]], strokeColor=Theme.BORDER),
        b.rectangle(470,350,100,40, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(470,350,"Save", width=100, height=40, textAlign="center", verticalAlign="middle", strokeColor=Theme.PRIMARY_FG),
    ])

    # Data visualization
    b.add_item("B/Data/Timeline", [
        b.line(20,0, [[0,0], [0,200]], strokeColor=Theme.BORDER),
        b.ellipse(15,0,10,10, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(40, -5, "v1.0.0 Released", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(40, 15, "Initial launch to public.", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.ellipse(15,80,10,10, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(40, 75, "v1.1.0 Beta", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(40, 95, "Testing new features.", fontSize=12, strokeColor=Theme.MUTED_FG),
    ])
    b.add_item("B/Data/KanbanColumn", [
        b.rectangle(0,0,260,600, backgroundColor=Theme.SECONDARY, strokeColor="transparent"),
        b.text(10,10,"In Progress", fontSize=14, extra={"fontWeight": "bold"}),
        b.rectangle(10,40,240,80, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,50,"Fix header bug", fontSize=14),
        b.rectangle(20,90,40,20, backgroundColor=Theme.DESTRUCTIVE_BG, fillStyle="solid"),
        b.text(25,92,"Bug", fontSize=10, strokeColor=Theme.DESTRUCTIVE),
        b.rectangle(10,130,240,80, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,140,"Update docs", fontSize=14),
    ])

    # Additional missing modules - Part 1
    b.add_item("B/Accordion/Item", [
        b.rectangle(0,0,400,50, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,15,"Is it accessible?", fontSize=16, extra={"fontWeight": "bold"}),
        b.line(0,0, [[370,20], [375,25], [380,20]], strokeColor=Theme.FOREGROUND)
    ])
    b.add_item("B/Accordion/Item/Expanded", [
        b.rectangle(0,0,400,140, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,15,"Is it accessible?", fontSize=16, extra={"fontWeight": "bold"}),
        b.line(0,0, [[370,25], [375,20], [380,25]], strokeColor=Theme.FOREGROUND),
        b.line(0,55, [[20,0], [380,0]], strokeColor=Theme.BORDER),
        b.text(20,75,"Yes. It adheres to the WAI-ARIA design pattern.", fontSize=14, strokeColor=Theme.MUTED_FG)
    ])
    b.add_item("B/Calendar", [
        b.rectangle(0,0,280,280, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,15,"January 2024", fontSize=16, extra={"fontWeight": "bold"}),
        b.line(0,45, [[0,0], [280,0]], strokeColor=Theme.BORDER),
        # Weekday headers
        b.text(20,60,"Su", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(60,60,"Mo", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(100,60,"Tu", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(140,60,"We", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(180,60,"Th", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(220,60,"Fr", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(260,60,"Sa", fontSize=12, strokeColor=Theme.MUTED_FG),
        # Sample dates
        b.text(20,90,"1", fontSize=14),
        b.text(60,90,"2", fontSize=14),
        b.ellipse(95,85,30,30, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(100,90,"3", fontSize=14, strokeColor=Theme.PRIMARY_FG),
        b.text(140,90,"4", fontSize=14),
    ])
    b.add_item("B/Carousel", [
        b.rectangle(0,0,400,250, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.text(0,0,"[Image]", width=400, height=250, textAlign="center", verticalAlign="middle", fontSize=20, strokeColor=Theme.MUTED_FG),
        # Indicators
        b.ellipse(170,220,8,8, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.ellipse(190,220,8,8, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.ellipse(210,220,8,8, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        # Nav arrows
        b.rectangle(10,110,30,30, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.line(0,0, [[25,120], [20,125], [25,130]], strokeColor=Theme.FOREGROUND),
        b.rectangle(360,110,30,30, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.line(0,0, [[365,120], [370,125], [365,130]], strokeColor=Theme.FOREGROUND),
    ])
    b.add_item("B/Collapsible", [
        b.rectangle(0,0,300,50, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,15,"@peduarte starred 3 repositories", fontSize=14),
        b.line(0,0, [[270,20], [275,25], [280,20]], strokeColor=Theme.MUTED_FG)
    ])

    # Additional missing modules - Part 2
    b.add_item("B/Command/Palette", [
        b.rectangle(0,0,500,350, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.rectangle(20,20,460,40, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.ellipse(35,32,16,16, strokeColor=Theme.MUTED_FG),
        b.text(60,28,"Type a command or search...", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.line(0,75, [[0,0], [500,0]], strokeColor=Theme.BORDER),
        b.text(20,95,"Suggestions", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.rectangle(20,115,460,35, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(35,123,"Calendar", fontSize=14),
        b.text(35,160,"Search Emoji", fontSize=14),
        b.text(35,195,"Calculator", fontSize=14),
    ])
    b.add_item("B/ContextMenu", [
        b.rectangle(0,0,180,200, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(15,15,"Back", fontSize=14),
        b.text(135,15,"⌘[", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(15,45,"Forward", fontSize=14),
        b.text(135,45,"⌘]", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(15,75,"Reload", fontSize=14),
        b.text(135,75,"⌘R", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.line(0,100, [[0,0], [180,0]], strokeColor=Theme.BORDER),
        b.text(15,115,"Save Page As...", fontSize=14),
        b.text(15,145,"Print...", fontSize=14),
        b.text(135,145,"⌘P", fontSize=12, strokeColor=Theme.MUTED_FG),
    ])
    b.add_item("B/HoverCard", [
        b.rectangle(0,0,280,140, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.ellipse(15,15,40,40, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.text(65,15,"@nextjs", fontSize=16, extra={"fontWeight": "bold"}),
        b.text(65,40,"The React Framework", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.text(15,80,"Created March 2023", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(15,105,"1.2M followers", fontSize=12, strokeColor=Theme.MUTED_FG),
    ])
    b.add_item("B/Popover", [
        b.rectangle(0,0,250,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(15,15,"Dimensions", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(15,45,"Width", fontSize=12),
        b.rectangle(15,65,100,30, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(25,73,"100%", fontSize=14),
        # Arrow
        b.line(0,0, [[125,-10], [135,-20]], strokeColor=Theme.BORDER),
        b.line(0,0, [[125,-10], [135,0]], strokeColor=Theme.BORDER),
    ])
    b.add_item("B/Tooltip", [
        b.rectangle(0,0,120,35, backgroundColor=Theme.FOREGROUND, fillStyle="solid"),
        b.text(0,0,"Add to library", width=120, height=35, textAlign="center", verticalAlign="middle", fontSize=12, strokeColor=Theme.BACKGROUND),
        # Arrow
        b.line(0,0, [[55,35], [60,42], [65,35]], strokeColor=Theme.FOREGROUND, fillStyle="solid")
    ])

    # Additional missing modules - Part 3
    b.add_item("B/Menubar", [
        b.rectangle(0,0,600,40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(15,12,"File", fontSize=14),
        b.text(60,12,"Edit", fontSize=14),
        b.text(105,12,"View", fontSize=14),
        b.text(160,12,"Help", fontSize=14),
    ])
    b.add_item("B/NavigationMenu", [
        b.rectangle(0,0,500,40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,12,"Getting Started", fontSize=14),
        b.text(140,12,"Components", fontSize=14),
        b.line(0,0, [[230,17], [235,22], [240,17]], strokeColor=Theme.MUTED_FG),
        b.text(260,12,"Documentation", fontSize=14),
    ])
    b.add_item("B/Resizable/Panels", [
        b.rectangle(0,0,600,300, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.line(0,0, [[300,0], [300,300]], strokeColor=Theme.BORDER),
        b.text(120,140,"Panel 1", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.text(420,140,"Panel 2", fontSize=16, strokeColor=Theme.MUTED_FG),
        # Resize handle
        b.rectangle(295,140,10,20, backgroundColor=Theme.MUTED, fillStyle="solid"),
    ])
    b.add_item("B/ScrollArea", [
        b.rectangle(0,0,300,200, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(15,15,"Item 1", fontSize=14),
        b.text(15,45,"Item 2", fontSize=14),
        b.text(15,75,"Item 3", fontSize=14),
        b.text(15,105,"Item 4", fontSize=14),
        b.text(15,135,"Item 5", fontSize=14),
        # Scrollbar
        b.rectangle(285,10,6,180, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.rectangle(285,10,6,50, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
    ])
    b.add_item("B/Sheet", [
        b.rectangle(0,0,400,600, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(20,20,"Edit Profile", fontSize=24, extra={"fontWeight": "bold"}),
        b.line(0,0, [[370,25], [375,20], [380,25]], strokeColor=Theme.MUTED_FG),
        b.line(0,70, [[0,0], [400,0]], strokeColor=Theme.BORDER),
        b.text(20,90,"Make changes to your profile here.", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.text(20,130,"Name", fontSize=14),
        b.rectangle(20,155,360,40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
    ])
