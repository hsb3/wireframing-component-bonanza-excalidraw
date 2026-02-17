from excalidraw_gen.core.themes.default import Theme

def add_saas_blocks(b):
    """High Level SaaS Patterns"""
    # Sidebar
    h = 500
    w = 240
    b.add_item("SaaS: Sidebar", [
        b.rectangle(0,0,w,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.rectangle(16,16,32,32, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(60,20,"Acme Inc", fontSize=20, extra={"fontWeight": "bold"}),
        
        b.text(16,70,"Platform", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.rectangle(8,90,224,36, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(40,96,"Dashboard", fontSize=16),
        b.text(40,132,"Analytics", fontSize=16),
        b.text(40,168,"Settings", fontSize=16),
        
        b.text(16,220,"Projects", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.text(40,245,"Design System", fontSize=16),
        
        b.line(0,0, [[0,h-60],[w,h-60]], strokeColor=Theme.BORDER),
        b.ellipse(16,h-45,32,32, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.text(60,h-40,"Admin", fontSize=16)
    ])
    
    # Navbar
    nav_w = 800
    b.add_item("SaaS: Navbar", [
        b.rectangle(0,0,nav_w,60, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,18,"Logo", fontSize=20, extra={"fontWeight": "bold"}),
        b.text(100,20,"Overview", fontSize=16),
        b.text(200,20,"Customers", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.rectangle(nav_w-250, 12, 180, 36, backgroundColor=Theme.MUTED, strokeColor="transparent"),
        b.text(nav_w-240, 18, "Search...", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.ellipse(nav_w-50, 15, 30, 30, backgroundColor=Theme.MUTED, fillStyle="solid")
    ])
    
    # Generic Header
    b.add_item("SaaS: Page Header", [
       b.text(0,0,"Dashboard", fontSize=30, extra={"fontWeight": "bold"}),
       b.text(0,40,"Overview of your key metrics.", fontSize=16, strokeColor=Theme.MUTED_FG),
       b.rectangle(600,0,140,40, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
       b.text(600,0,"Download", width=140, height=40, textAlign="center", verticalAlign="middle", strokeColor=Theme.PRIMARY_FG)
    ])
    
    # Metric Card
    b.add_item("SaaS: Metric Card", [
        b.rectangle(0,0,240,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,20,"Total Revenue", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(20,50,"$45,231.89", fontSize=28, extra={"fontWeight": "bold"}),
        b.text(20,90,"+20.1% from last month", fontSize=12, strokeColor=Theme.MUTED_FG)
    ])
    
    # Chart Placeholder
    b.add_item("SaaS: Chart (Bar)", [
        b.rectangle(0,0,400,200, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,10,"Overview", fontSize=16, extra={"fontWeight": "bold"}),
        b.rectangle(30,50,40,120, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.rectangle(90,80,40,90, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.rectangle(150,40,40,130, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
    ])
    
    # Data Table
    b.add_item("SaaS: Data Table", [
        b.rectangle(0,0,600,200, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.line(0,0, [[0,40], [600,40]], strokeColor=Theme.BORDER),
        b.text(20,10,"ID", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(100,10,"Status", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(250,10,"Email", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(450,10,"Amount", fontSize=14, extra={"fontWeight": "bold"}),
        # Row 1
        b.text(20,55,"#123", fontSize=14),
        b.text(100,55,"Success", fontSize=14),
        b.text(250,55,"ken@example.com", fontSize=14),
        b.text(450,55,"$350.00", fontSize=14),
        b.line(0,0, [[0,90], [600,90]], strokeColor=Theme.BORDER),
        # Row 2
        b.text(20,105,"#124", fontSize=14),
        b.text(100,105,"Processing", fontSize=14),
        b.text(250,105,"abe@example.com", fontSize=14),
        b.text(450,105,"$200.00", fontSize=14),
    ])

    # Login Form
    b.add_item("SaaS: Login Form", [
        b.rectangle(0,0,360,340, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(30,30,"Login", fontSize=24, extra={"fontWeight": "bold"}),
        b.text(30,65,"Enter your email below to login.", fontSize=14, strokeColor=Theme.MUTED_FG),
        
        b.text(30,100,"Email", fontSize=14),
        b.rectangle(30,125,300,40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(40,135,"m@example.com", fontSize=14),
        
        b.text(30,180,"Password", fontSize=14),
        b.rectangle(30,205,300,40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        
        b.rectangle(30,265,300,40, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(30,265,"Sign In", width=300, height=40, textAlign="center", verticalAlign="middle", strokeColor=Theme.PRIMARY_FG)
    ])

    # Advanced Data Patterns
    b.add_item("SaaS: CRUD Table (+Filters)", [
        b.rectangle(0,0,800,400, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        # Toolbar
        b.text(20,20,"Customers", fontSize=20, extra={"fontWeight": "bold"}),
        b.rectangle(20, 60, 200, 36, strokeColor=Theme.INPUT),
        b.text(30, 68, "Filter email...", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.rectangle(230, 60, 100, 36, strokeColor=Theme.INPUT, lineStyle="dashed"),
        b.text(250, 68, "Status +", fontSize=14),
        b.rectangle(660, 60, 120, 36, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(660, 60, "Add New", width=120, height=36, textAlign="center", verticalAlign="middle", strokeColor=Theme.PRIMARY_FG),
        
        # Table Header
        b.line(0,0, [[0,110], [800,110]], strokeColor=Theme.BORDER),
        b.text(20,120,"Name", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(200,120,"Status", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(400,120,"Role", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(750,120,"...", fontSize=14, extra={"fontWeight": "bold"}),
        
        # Rows
        b.text(20,150,"Alice Smith", fontSize=14),
        b.rectangle(200,148, 60, 24, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(200,148,"Active", width=60, height=24, textAlign="center", verticalAlign="middle", fontSize=12),
        b.text(400,150,"Admin", fontSize=14),
        b.text(750,150,"...", fontSize=14),
        b.line(0,0, [[0,180], [800,180]], strokeColor=Theme.BORDER),
    ])

    b.add_item("SaaS: Metrics Grid", [
        # Card 1
        b.rectangle(0,0,240,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,20,"Revenue", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(20,45,"$45,231", fontSize=24),
        b.text(20,80,"+20%", fontSize=12, strokeColor=Theme.MUTED_FG),
        # Card 2
        b.rectangle(260,0,240,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(280,20,"Subscriptions", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(280,45,"2,350", fontSize=24),
        b.text(280,80,"+180", fontSize=12, strokeColor=Theme.MUTED_FG),
        # Card 3
        b.rectangle(520,0,240,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(540,20,"Active Now", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(540,45,"573", fontSize=24),
        b.text(540,80,"+201", fontSize=12, strokeColor=Theme.MUTED_FG),
    ])
    
    b.add_item("SaaS: Faceted Search", [
       b.rectangle(0,0,200,600, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
       b.text(20,20,"Filters", fontSize=18, extra={"fontWeight": "bold"}),
       b.text(20,60,"Category", fontSize=14, extra={"fontWeight": "bold"}),
       b.rectangle(20,85,16,16, strokeColor=Theme.BORDER),
       b.text(45,85,"Electronics", fontSize=14),
       b.rectangle(20,110,16,16, strokeColor=Theme.BORDER),
       b.text(45,110,"Clothing", fontSize=14),
       b.text(20,150,"Price Range", fontSize=14, extra={"fontWeight": "bold"}),
       b.rectangle(20,180,160,4, backgroundColor=Theme.INPUT, fillStyle="solid"),
       b.rectangle(20,180,80,4, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
       
       b.rectangle(220, 0, 600, 600, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, strokeStyle="dashed"),
       b.text(450, 280, "Results Grid", fontSize=16, strokeColor=Theme.MUTED_FG)
    ])
