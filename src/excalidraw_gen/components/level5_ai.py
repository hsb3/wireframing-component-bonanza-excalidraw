from excalidraw_gen.core.themes.mork import Theme

def add_ai_patterns(b):
    """AI & Chat Patterns"""
    # User Msg
    b.add_item("AI: User Bubble", [
        b.rectangle(0,0,300,50, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(15,12,"Generate a component", fontSize=16, strokeColor=Theme.PRIMARY_FG)
    ])
    
    # AI Msg
    b.add_item("AI: Response Bubble", [
        b.ellipse(0,0,30,30, backgroundColor=Theme.BORDER, fillStyle="solid"),
        b.rectangle(40,0,320,80, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(55,10,"Here is the component you requested.", width=290, height=60, fontSize=16)
    ])
    
    # Input
    b.add_item("AI: Prompt Input", [
        b.rectangle(0,0,600,60, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20,20,"Ask AI assistant...", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.rectangle(550,10,40,40, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.line(0,0, [[565,30], [580,30]], strokeColor=Theme.PRIMARY_FG), 
    ])
    
    # Code Block
    b.add_item("AI: Code Artifact", [
        b.rectangle(0,0,400,120, backgroundColor=Theme.ACCENT, strokeColor=Theme.BORDER),
        b.text(10,5, "tsx", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(15,30, "export function Button() {\n  return <button>Click me</button>\n}", fontFamily=Theme.FONT_CODE, fontSize=14)
    ])
    
    # Thinking
    b.add_item("AI: Thinking", [
        b.ellipse(0,0,8,8, backgroundColor=Theme.MUTED_FG, fillStyle="solid"),
        b.ellipse(15,0,8,8, backgroundColor=Theme.MUTED_FG, fillStyle="solid", opacity=60),
        b.ellipse(30,0,8,8, backgroundColor=Theme.MUTED_FG, fillStyle="solid", opacity=30),
    ])
    
    # Thread View
    b.add_item("AI: Chat Thread", [
        b.rectangle(0,0,400,500, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        # Header
        b.line(0,0, [[0,50],[400,50]], strokeColor=Theme.BORDER),
        b.text(20,15, "Chat Assistant", fontWeight="bold"),
        # Messages
        b.text(20, 70, "User: Help me design", fontSize=14),
        b.text(20, 100, "AI: Sure thing...", fontSize=14, strokeColor=Theme.MUTED_FG),
        # Input
        b.rectangle(20, 440, 360, 40, strokeColor=Theme.BORDER),
    ])

    # AI Advanced
    b.add_item("AI: Tool Call (Card)", [
         b.rectangle(0,0,300,50, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
         b.text(10,12,"🔨 searching_web('excalidraw')", fontFamily=Theme.FONT_CODE, fontSize=12),
         b.line(270,20, [[0,0], [10,10]], strokeColor=Theme.MUTED_FG), # chevron down
    ])
    
    b.add_item("AI: Citations (Inline)", [
         b.text(0,0,"According to recent stats", fontSize=16),
         b.rectangle(190,0,20,20, backgroundColor=Theme.MUTED),
         b.text(196,2,"1", fontSize=12, strokeColor=Theme.MUTED_FG),
         b.text(215,0,"the market is growing.", fontSize=16)
    ])

    b.add_item("AI: Streaming Cursor", [
         b.text(0,0,"The concept of ", fontSize=16),
         b.ellipse(120,5,10,10, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
    ])

    b.add_item("AI: Message Meta", [
         b.text(0,0, "Avatar", fontSize=12, strokeColor=Theme.MUTED_FG),
         b.text(50,0, "Today at 2:30 PM", fontSize=12, strokeColor=Theme.MUTED_FG),
         b.rectangle(160,0,16,16, strokeColor=Theme.MUTED_FG), # Copy icon
         b.rectangle(185,0,16,16, strokeColor=Theme.MUTED_FG), # Retry icon
    ])

    # Additional chat components from generate_library
    b.add_item("C/Block/Chat/SidebarThreadList", [
        b.rectangle(0,0,260,600, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.rectangle(15,15,230,36, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, strokeStyle="dashed"),
        b.text(30,22,"+ New Chat", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.text(20,70,"Today", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(20,95,"Project Analytics Q3", fontSize=14),
        b.text(20,125,"React Component Help", fontSize=14),
        b.text(20,165,"Previous 7 Days", fontSize=12, strokeColor=Theme.MUTED_FG),
        b.text(20,190,"Debug Python Script", fontSize=14),
    ])
    b.add_item("C/Block/Chat/MessageBubble/User", [
        b.rectangle(0,0,400,60, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.text(20, 20, "Can you explain the error trace?", fontSize=16)
    ])
    b.add_item("C/Block/Chat/MessageBubble/Assistant", [
        b.ellipse(0,0,32,32, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
        b.text(50, 0, "AI Assistant", fontSize=14, extra={"fontWeight": "bold"}),
        b.text(50, 25, "The error suggests a timeout in the database connection pool.", fontSize=16, width=500),
    ])
    b.add_item("C/Block/Chat/Thinking", [
        b.text(0,0,"Thinking...", fontSize=14, strokeColor=Theme.MUTED_FG),
        b.ellipse(80,8,4,4, backgroundColor=Theme.MUTED_FG, fillStyle="solid"),
        b.ellipse(90,8,4,4, backgroundColor=Theme.MUTED_FG, fillStyle="solid"),
        b.ellipse(100,8,4,4, backgroundColor=Theme.MUTED_FG, fillStyle="solid"),
    ])
    b.add_item("C/Block/Chat/ToolCallCard", [
        b.rectangle(0,0,500,40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(15,10,"Executed script: analyze_data.py", fontSize=14, strokeColor=Theme.MUTED_FG, fontFamily=Theme.FONT_CODE),
        b.line(0,0, [[470,15], [475,20], [480,15]], strokeColor=Theme.MUTED_FG),
    ])
    b.add_item("C/Block/Chat/Artifact/Code", [
        b.rectangle(0,0,500,200, backgroundColor=Theme.SECONDARY, strokeColor=Theme.BORDER),
        b.rectangle(0,0,500,30, backgroundColor=Theme.BORDER, fillStyle="solid"),
        b.text(10,5,"index.ts", fontSize=12, fontFamily=Theme.FONT_CODE),
        b.text(10,40,"export const data = [];", fontSize=14, fontFamily=Theme.FONT_CODE, strokeColor=Theme.MUTED_FG),
    ])
    b.add_item("C/Block/Chat/Composer", [
        b.rectangle(0,0,700,100, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
        b.text(20, 20, "Type a message...", fontSize=16, strokeColor=Theme.MUTED_FG),
        b.rectangle(20, 60, 24, 24, backgroundColor=Theme.SECONDARY, fillStyle="solid"),
        b.rectangle(640, 50, 40, 40, backgroundColor=Theme.PRIMARY, fillStyle="solid"),
    ])
