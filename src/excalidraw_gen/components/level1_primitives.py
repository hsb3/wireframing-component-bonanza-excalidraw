from excalidraw_gen.core.themes.default import Theme

def add_primitives(b):
    """Typography and Icons"""
    # Typography
    b.add_item("Type: H1", [b.text(0, 0, "Heading 1", fontSize=36, extra={"fontWeight": "bold"})])
    b.add_item("Type: H2", [b.text(0, 0, "Heading 2", fontSize=30, extra={"fontWeight": "bold"})])
    b.add_item("Type: H3", [b.text(0, 0, "Heading 3", fontSize=24, extra={"fontWeight": "bold"})])
    b.add_item("Type: Body", [b.text(0, 0, "The quick brown fox jumps over the lazy dog.", fontSize=20, strokeColor=Theme.MUTED_FG)])
    b.add_item("Type: Small", [b.text(0, 0, "Small text description", fontSize=16, strokeColor=Theme.MUTED_FG)])
    
    # Icons (Constructed from lines)
    b.add_item("Icon: Search", [
        b.ellipse(0,0,20,20, strokeColor=Theme.MUTED_FG),
        b.line(0,0, [[15,15], [22,22]], strokeColor=Theme.MUTED_FG, strokeWidth=2)
    ])
    b.add_item("Icon: User", [
        b.ellipse(5,0,14,14, strokeColor=Theme.MUTED_FG),
        b.line(0,0, [[0,24], [2,18], [12,14], [22,18], [24,24]], strokeColor=Theme.MUTED_FG)
    ])
    b.add_item("Icon: Settings", [
        b.ellipse(0,0,24,24, strokeColor=Theme.MUTED_FG, strokeStyle="dashed"),
        b.ellipse(8,8,8,8, strokeColor=Theme.MUTED_FG),
    ])
    b.add_item("Icon: Close", [
        b.line(0,0, [[0,0], [16,16]], strokeColor=Theme.MUTED_FG),
        b.line(0,0, [[16,0], [0,16]], strokeColor=Theme.MUTED_FG)
    ])
    b.add_item("Icon: Menu", [
        b.line(0,0, [[0,0], [24,0]], strokeColor=Theme.MUTED_FG),
        b.line(0,8, [[0,8], [24,8]], strokeColor=Theme.MUTED_FG),
        b.line(0,16, [[0,16], [24,16]], strokeColor=Theme.MUTED_FG)
    ])

    # Additional Atoms from generate_library
    b.add_item("A/Text/Link", [
        b.text(0, 0, "Link Text", fontSize=16, strokeColor=Theme.INFO, extra={"textDecoration": "underline"})
    ])
    b.add_item("A/Text/CodeInline", [
        b.text(0, 0, "const x = 42;", fontSize=16, fontFamily=Theme.FONT_CODE, strokeColor=Theme.FOREGROUND)
    ])

    # Icons/Avatars
    b.add_item("A/Icon/Placeholder", [
        b.rectangle(0,0,24,24, backgroundColor="transparent", strokeColor=Theme.MUTED_FG),
        b.line(0,0, [[0,0], [24,24]], strokeColor=Theme.MUTED_FG),
        b.line(0,0, [[24,0], [0,24]], strokeColor=Theme.MUTED_FG)
    ])
    b.add_item("A/Avatar/Circle", [
        b.ellipse(0,0,40,40, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.text(0,0,"JD", width=40, height=40, textAlign="center", verticalAlign="middle", strokeColor=Theme.MUTED_FG)
    ])

    # Controls & Status
    b.add_item("A/Button/Loading", [
        b.rectangle(0,0,120,40, backgroundColor=Theme.PRIMARY, fillStyle="solid", opacity=80),
        b.ellipse(50,10,20,20, strokeColor=Theme.PRIMARY_FG, strokeStyle="dashed")
    ])
    b.add_item("A/Badge/Status", [
        b.rectangle(0,0,60,22, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.text(0,0,"Status", width=60, height=22, textAlign="center", verticalAlign="middle", strokeColor=Theme.MUTED_FG, fontSize=12)
    ])
    b.add_item("A/Stepper", [
         b.ellipse(0,0,24,24, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
         b.text(8,2,"1", fontSize=14, strokeColor=Theme.PRIMARY_FG),
         b.line(24,12, [[0,0], [40,0]], strokeColor=Theme.BORDER),
         b.ellipse(64,0,24,24, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
         b.text(72,2,"2", fontSize=14, strokeColor=Theme.MUTED_FG),
         b.line(88,12, [[0,0], [40,0]], strokeColor=Theme.BORDER),
         b.ellipse(128,0,24,24, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
         b.text(136,2,"3", fontSize=14, strokeColor=Theme.MUTED_FG),
    ])
    b.add_item("A/Progress/Bar", [
        b.rectangle(0,0,200,8, backgroundColor=Theme.INPUT, fillStyle="solid"),
        b.rectangle(0,0,120,8, backgroundColor=Theme.PRIMARY, fillStyle="solid")
    ])
    b.add_item("A/Alert/Info", [
        b.rectangle(0,0,400,50, backgroundColor=Theme.INFO_BG, strokeColor=Theme.INFO_BORDER, fillStyle="solid"),
        b.text(20,15,"This is an informational message.", fontSize=16, strokeColor=Theme.INFO_TEXT)
    ])
    b.add_item("A/Skeleton/Line", [
        b.rectangle(0,0,200,20, backgroundColor=Theme.MUTED, fillStyle="solid", strokeColor="transparent")
    ])
    b.add_item("A/EmptyState", [
        b.ellipse(0,0,80,80, backgroundColor=Theme.MUTED, fillStyle="solid"),
        b.text(0,100,"No projects found", width=80, textAlign="center", fontSize=16, extra={"fontWeight": "bold"}),
        b.text(-40,130,"Get started by creating a new project.", width=160, textAlign="center", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.rectangle(-20,160,120,40, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(-20,160,"Create Project", width=120, height=40, textAlign="center", verticalAlign="middle"),
    ])

    # Additional missing primitives
    b.add_item("A/Spinner", [
        b.ellipse(0,0,24,24, strokeColor=Theme.PRIMARY, strokeStyle="dashed", strokeWidth=2),
        b.line(12,0, [[0,0], [0,-12]], strokeColor=Theme.PRIMARY, strokeWidth=2)
    ])
    b.add_item("A/Separator/Horizontal", [
        b.line(0,0, [[0,0], [200,0]], strokeColor=Theme.BORDER)
    ])
    b.add_item("A/Separator/Vertical", [
        b.line(0,0, [[0,0], [0,200]], strokeColor=Theme.BORDER)
    ])
    b.add_item("A/Kbd", [
        b.rectangle(0,0,40,28, backgroundColor=Theme.MUTED, strokeColor=Theme.BORDER, fillStyle="solid"),
        b.text(0,0,"⌘K", width=40, height=28, textAlign="center", verticalAlign="middle", fontSize=14, fontFamily=Theme.FONT_CODE)
    ])
    b.add_item("A/Toggle", [
        b.rectangle(0,0,40,40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(0,0,"B", width=40, height=40, textAlign="center", verticalAlign="middle", fontSize=16, extra={"fontWeight": "bold"})
    ])
    b.add_item("A/Toggle/Active", [
        b.rectangle(0,0,40,40, backgroundColor=Theme.SECONDARY, strokeColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(0,0,"B", width=40, height=40, textAlign="center", verticalAlign="middle", fontSize=16, extra={"fontWeight": "bold"})
    ])
