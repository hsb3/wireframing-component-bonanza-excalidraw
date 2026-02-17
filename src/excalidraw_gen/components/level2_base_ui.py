from excalidraw_gen.core.themes.mork import Theme

def add_base_ui(b):
    """Buttons, Inputs, Controls"""
    h = Theme.BTN_HEIGHT
    
    # Buttons
    w = 120
    b.add_item("Button: Primary", [
        b.rectangle(0,0,w,h, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(0,0,"Action", width=w, height=h, textAlign="center", verticalAlign="middle", strokeColor=Theme.PRIMARY_FG)
    ])
    b.add_item("Button: Secondary", [
        b.rectangle(0,0,w,h, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(0,0,"Cancel", width=w, height=h, textAlign="center", verticalAlign="middle", strokeColor=Theme.SECONDARY_FG)
    ])
    b.add_item("Button: Outline", [
        b.rectangle(0,0,w,h, backgroundColor="transparent", strokeColor=Theme.BORDER),
        b.text(0,0,"Outline", width=w, height=h, textAlign="center", verticalAlign="middle", strokeColor=Theme.FOREGROUND)
    ])
    b.add_item("Button: Ghost", [
        b.rectangle(0,0,w,h, backgroundColor="transparent", strokeColor="transparent"),
        b.text(0,0,"Ghost", width=w, height=h, textAlign="center", verticalAlign="middle", strokeColor=Theme.FOREGROUND)
    ])
    b.add_item("Button: Destructive", [
        b.rectangle(0,0,w,h, backgroundColor=Theme.DESTRUCTIVE, fillStyle="solid"),
        b.text(0,0,"Delete", width=w, height=h, textAlign="center", verticalAlign="middle", strokeColor=Theme.DESTRUCTIVE_FG)
    ])
    b.add_item("Button: Link", [
        b.text(0,0,"Click here", strokeColor=Theme.PRIMARY, fontSize=16, extra={"textDecoration": "underline"})
    ])
    
    # Inputs
    w_inp = Theme.INPUT_WIDTH
    b.add_item("Input: Text", [
        b.rectangle(0,0,w_inp,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(10,8,"Email address...", fontSize=16, strokeColor=Theme.MUTED_FG)
    ])
    b.add_item("Input: Search", [
        b.rectangle(0,0,w_inp,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.ellipse(12,12,14,14, strokeColor=Theme.MUTED_FG), # icon mock
        b.text(35,8,"Search...", fontSize=16, strokeColor=Theme.MUTED_FG)
    ])
    b.add_item("Input: Select", [
        b.rectangle(0,0,200,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(10,8,"Select option", fontSize=16, strokeColor=Theme.FOREGROUND),
        b.line(0,0, [[180, 15], [185, 20], [190, 15]], strokeColor=Theme.MUTED_FG)
    ])
    b.add_item("Input: Textarea", [
        b.rectangle(0,0,w_inp,100, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(10,8,"Type description...", fontSize=16, strokeColor=Theme.MUTED_FG)
    ])
    b.add_item("Input: Date Picker", [
        b.rectangle(0,0,200,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(10,8,"Pick a date", fontSize=16, strokeColor=Theme.FOREGROUND),
        b.rectangle(170,10,20,20, strokeColor=Theme.MUTED_FG) # Calendar icon
    ])
    
    # Toggles
    b.add_item("Control: Checkbox", [
        b.rectangle(0,0,20,20, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.PRIMARY),
        b.text(30, -2, "Remember me", fontSize=16) 
    ])
    b.add_item("Control: Checkbox (Active)", [
        b.rectangle(0,0,20,20, backgroundColor=Theme.PRIMARY, fillStyle="solid", strokeColor=Theme.PRIMARY),
        b.line(0,0, [[4,10],[8,14],[14,4]], strokeColor=Theme.PRIMARY_FG, strokeWidth=2),
    ])
    b.add_item("Control: Radio", [
        b.ellipse(0,0,20,20, strokeColor=Theme.PRIMARY),
        b.text(30,-2, "Option", fontSize=16)
    ])
    b.add_item("Control: Radio (Active)", [
        b.ellipse(0,0,20,20, strokeColor=Theme.PRIMARY),
        b.ellipse(5,5,10,10, backgroundColor=Theme.PRIMARY, fillStyle="solid")
    ])
    b.add_item("Control: Switch", [
        b.rectangle(0,0,44,24, backgroundColor=Theme.INPUT, fillStyle="solid", roundness={"type": 20}),
        b.ellipse(2,2,20,20, backgroundColor=Theme.BACKGROUND, fillStyle="solid")
    ])
    b.add_item("Control: Slider", [
        b.rectangle(0,8,200,4, backgroundColor=Theme.INPUT, fillStyle="solid"),
        b.rectangle(0,8,80,4, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.ellipse(70,0,20,20, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER)
    ])

    # Advanced Inputs
    b.add_item("Input: Search Bar", [
        b.rectangle(0,0,300,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.ellipse(15,12,16,16, strokeColor=Theme.MUTED_FG),
        b.text(40,8,"Search customers...", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.rectangle(250,5,40,30, backgroundColor=Theme.MUTED, strokeColor="transparent"),
        b.text(255,10,"⌘K", fontSize=12, strokeColor=Theme.MUTED_FG) 
    ])
    
    b.add_item("Input: Button Group", [
        b.rectangle(0,0,80,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(0,0,"Years", width=80, height=h, textAlign="center", verticalAlign="middle", fontSize=14),
        b.rectangle(80,0,80,h, backgroundColor=Theme.PRIMARY, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(80,0,"Months", width=80, height=h, textAlign="center", verticalAlign="middle", fontSize=14, strokeColor=Theme.PRIMARY_FG),
        b.rectangle(160,0,80,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(160,0,"Days", width=80, height=h, textAlign="center", verticalAlign="middle", fontSize=14),
    ])

    b.add_item("Input: Upload Dropzone", [
        b.rectangle(0,0,400,150, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, strokeStyle="dashed"),
        b.ellipse(180,30,40,40, strokeColor=Theme.MUTED_FG), # cloud icon
        b.text(0,80,"Drag & drop files here", width=400, textAlign="center", fontSize=16, strokeColor=Theme.FOREGROUND),
        b.text(0,110,"or click to browse", width=400, textAlign="center", fontSize=14, strokeColor=Theme.MUTED_FG)
    ])

    b.add_item("Input: Amount", [
        b.rectangle(0,0,40,h, backgroundColor=Theme.MUTED, strokeColor=Theme.INPUT),
        b.text(0,0,"$", width=40, height=h, textAlign="center", verticalAlign="middle"),
        b.rectangle(40,0,160,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(50,8,"0.00", fontSize=16)
    ])
    
    # Form Field Wrappers
    b.add_item("Form: Field (Label+Input)", [
        b.text(0,0,"Email", fontSize=14, extra={"fontWeight": "bold"}),
        b.rectangle(0,25,250,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
    ])
    b.add_item("Form: Field (Error)", [
        b.text(0,0,"Email", fontSize=14, extra={"fontWeight": "bold"}),
        b.rectangle(0,25,250,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.DESTRUCTIVE),
        b.text(0,70,"Invalid email address", fontSize=12, strokeColor=Theme.DESTRUCTIVE)
    ])
    b.add_item("Form: OTP Input", [
        b.rectangle(0,0,40,50, strokeColor=Theme.INPUT),
        b.rectangle(50,0,40,50, strokeColor=Theme.INPUT),
        b.rectangle(100,0,40,50, strokeColor=Theme.INPUT),
        b.rectangle(150,0,40,50, strokeColor=Theme.INPUT),
        b.text(16,12,"5", fontSize=24),
    ])

    # Additional inputs from generate_library
    b.add_item("B/Form/Input/Number", [
        b.text(0,0, "Quantity", fontSize=14, extra={"fontWeight": "bold"}),
        b.rectangle(0,25,280,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(10,35,"1", fontSize=16),
        b.line(0,0, [[250,25], [250,65]], strokeColor=Theme.INPUT),
        b.line(0,0, [[250,45], [280,45]], strokeColor=Theme.INPUT),
        b.line(0,0, [[260,38], [270,32], [280,38]], strokeColor=Theme.MUTED_FG),
        b.line(0,0, [[260,52], [270,58], [280,52]], strokeColor=Theme.MUTED_FG),
    ])
    b.add_item("B/Form/Input/Slider", [
        b.text(0,0,"Volume", fontSize=14, extra={"fontWeight": "bold"}),
        b.rectangle(0,30,200,4, backgroundColor=Theme.INPUT, fillStyle="solid"),
        b.rectangle(0,30,120,4, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.ellipse(110,22,20,20, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(220,20,"60%", fontSize=14),
    ])
    b.add_item("B/Form/Input/ColorPicker", [
        b.text(0,0,"Accent Color", fontSize=14, extra={"fontWeight": "bold"}),
        b.rectangle(0,25,40,40, backgroundColor=Theme.DEMO_BLUE, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(50,35,"#3B82F6", fontSize=14, fontFamily=Theme.FONT_CODE),
    ])
    b.add_item("B/Form/Input/Tags", [
        b.text(0,0,"Tags", fontSize=14, extra={"fontWeight": "bold"}),
        b.rectangle(0,25,400,40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.rectangle(5,30,70,30, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(15,35,"React", fontSize=12),
        b.text(60,35,"x", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.rectangle(80,30,60,30, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(90,35,"Vue", fontSize=12),
        b.text(125,35,"x", fontSize=12, strokeColor=Theme.MUTED_FG),
    ])

    # Additional missing inputs
    b.add_item("B/Form/InputGroup/WithButton", [
        b.rectangle(0,0,200,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(10,8,"Search...", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.rectangle(200,0,80,h, backgroundColor=Theme.PRIMARY, fillStyle="solid", strokeColor=Theme.INPUT),
        b.text(200,0,"Search", width=80, height=h, textAlign="center", verticalAlign="middle", strokeColor=Theme.PRIMARY_FG)
    ])
    b.add_item("B/Form/InputGroup/WithIcon", [
        b.rectangle(0,0,250,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.ellipse(12,12,16,16, strokeColor=Theme.MUTED_FG),
        b.text(40,8,"name@example.com", fontSize=16, strokeColor=Theme.MUTED_FG)
    ])
    b.add_item("B/Form/InputGroup/WithAddon", [
        b.rectangle(0,0,60,h, backgroundColor=Theme.MUTED, fillStyle="solid", strokeColor=Theme.INPUT),
        b.text(0,0,"https://", width=60, height=h, textAlign="center", verticalAlign="middle", fontSize=14),
        b.rectangle(60,0,190,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(70,8,"example.com", fontSize=16)
    ])
    b.add_item("B/Form/Combobox", [
        b.text(0,0,"Framework", fontSize=14, extra={"fontWeight": "bold"}),
        b.rectangle(0,25,250,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(10,35,"Select framework...", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.line(0,0, [[230,35], [235,40], [240,35]], strokeColor=Theme.MUTED_FG),
        # Dropdown
        b.rectangle(0,70,250,120, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(10,80,"Next.js", fontSize=14),
        b.rectangle(0,100,250,30, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(10,108,"React", fontSize=14),
        b.text(10,138,"Vue", fontSize=14),
        b.text(10,168,"Svelte", fontSize=14)
    ])
    b.add_item("B/Form/Select/Enhanced", [
        b.text(0,0,"Select option", fontSize=14, extra={"fontWeight": "bold"}),
        b.rectangle(0,25,200,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(10,35,"Choose...", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.line(0,0, [[180,35], [185,40], [190,35]], strokeColor=Theme.MUTED_FG)
    ])
