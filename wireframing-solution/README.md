# Wireframe Copilot - AI-Powered Wireframe Generation

React app with embedded Excalidraw and LangGraph deep agent for generating wireframes from natural language.

## Architecture

```
Frontend (React + Excalidraw)
        ↕
Backend (LangGraph Deep Agent)
        ↕
Component Library (154 components × 3 themes)
```

## Quick Start

### 1. Setup Backend

```bash
cd wireframing-solution/backend

# Install dependencies
uv pip install -e .

# Generate component registry (first time only)
python scripts/generate_component_registry.py

# Create .env file
cp ../.env.example .env
# Add your ANTHROPIC_API_KEY
```

### 2. Setup Frontend

```bash
cd wireframing-solution/frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

### 3. Start Backend

```bash
cd wireframing-solution/backend

# Start LangGraph server
langgraph dev
# → Runs on http://localhost:8000
# → Serves React app at http://localhost:8000/app
```

### 4. Use the App

1. Open http://localhost:8000/app
2. Type in copilot: "Create a login screen with email and password"
3. Agent searches components, composes wireframe
4. Wireframe appears on Excalidraw canvas
5. Iterate: "Add a logo at the top"

---

## Project Structure

```
wireframing-solution/
├── langgraph.json                  # LangGraph configuration
├── .env.example                    # Environment template
│
├── backend/
│   ├── pyproject.toml             # Python dependencies
│   ├── src/
│   │   ├── agent/
│   │   │   ├── graph.py          # LangGraph deep agent
│   │   │   └── app.py            # FastAPI app
│   │   ├── tools/
│   │   │   └── composer.py       # Wireframe composition logic
│   │   └── data/
│   │       ├── component-registry.json  # Auto-generated
│   │       └── component-catalog.txt    # Human-readable
│   └── scripts/
│       └── generate_component_registry.py
│
├── frontend/
│   ├── package.json               # Node dependencies
│   ├── vite.config.ts            # Vite configuration
│   ├── src/
│   │   ├── main.tsx              # React entry point
│   │   ├── App.tsx               # Main app shell
│   │   └── components/
│   │       └── CopilotPanel.tsx  # AI chat interface
│   └── dist/                      # Built frontend (after npm run build)
│
└── wireframes/                     # Generated wireframes
    └── *.excalidraw
```

---

## Features

### Copilot Chat
- Natural language wireframe generation
- Real-time streaming responses
- Tool call visualization
- Message history

### Component Library Integration
- 154 pre-built components
- 3 themes (mork, abc123-dark, bronzer)
- Automatic component search
- Intelligent layout planning

### Excalidraw Canvas
- Embedded Excalidraw editor
- Live wireframe updates
- Full Excalidraw features (edit, export, etc.)
- Hand-drawn sketchy style

---

## Agent Tools

The LangGraph agent has access to:

### `search_components(query, theme, limit)`
Find components by keyword, category, or tags

### `get_component(component_id)`
Get full metadata for a specific component

### `compose_wireframe(name, theme, components)`
Generate .excalidraw file from component list

### `list_categories(theme)`
Browse available component categories

---

## Development

### Backend Development

```bash
cd backend

# Run with auto-reload
langgraph dev

# Or run FastAPI directly
uvicorn src.agent.app:app --reload --port 8000
```

### Frontend Development

```bash
cd frontend

# Dev server with HMR
npm run dev
# → http://localhost:5173

# Build for production
npm run build
# → dist/ folder
```

### Update Component Library

```bash
# After modifying component library in parent project
cd backend
python scripts/generate_component_registry.py
# Registry auto-updates, restart backend to load
```

---

## Example Usage

**Create login screen:**
```
User: "Create a login screen with email, password, and submit button"

Agent:
1. Searches: "login email password button"
2. Finds: B/Form/Input/Text (×2), Button: Primary
3. Composes wireframe at output/login.excalidraw
4. Responds: "Login screen created with 3 components"
```

**Iterate:**
```
User: "Add a logo above the form"

Agent:
1. Searches: "logo image icon"
2. Finds: Icon: Placeholder
3. Updates wireframe
4. Responds: "Added logo component at top"
```

**Complex dashboard:**
```
User: "Dashboard with sidebar, header, 3 metric cards, and data table"

Agent:
1. Searches multiple queries
2. Finds: C/Shell/App/3Pane, B/Nav/Header, SaaS/Metric/Card, SaaS/DataTable
3. Plans layout with appropriate spacing
4. Composes wireframe
5. Responds: "Dashboard created with 6 components arranged in layout"
```

---

## Deployment

### Local Development
```bash
langgraph dev
```

### LangSmith Deployment
```bash
langgraph deploy
```

### Docker (Future)
```yaml
version: '3.8'
services:
  wireframe-agent:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    volumes:
      - ./wireframes:/app/wireframes
      - ../output:/app/libraries:ro
```

---

## Extending

### Add New Tools

Edit `backend/src/agent/graph.py`:
```python
@tool
def my_custom_tool(arg: str) -> dict:
    """Tool description"""
    # Implementation
    return {}

# Add to tools list
graph = create_deep_agent(
    llm,
    tools=[..., my_custom_tool],
    system_message=SYSTEM_MESSAGE
)
```

### Customize Agent Prompt

Edit system message in `backend/src/agent/graph.py`

### Add UI Features

Edit `frontend/src/components/CopilotPanel.tsx` or create new components

---

## Troubleshooting

**Backend won't start:**
```bash
# Check Python version
python --version  # Should be 3.11+

# Install dependencies
cd backend && uv pip install -e .
```

**Frontend build fails:**
```bash
# Clear cache
rm -rf node_modules package-lock.json
npm install
```

**Agent can't find components:**
```bash
# Regenerate registry
python backend/scripts/generate_component_registry.py

# Check file exists
ls backend/src/data/component-registry.json
```

**Wireframes not appearing on canvas:**
- Check browser console for errors
- Verify Excalidraw API is initialized
- Check network tab for failed API calls

---

## Next Steps

1. ✅ Basic chat + canvas integration
2. TODO: Load generated wireframe into canvas automatically
3. TODO: Export to PNG from UI
4. TODO: Template library (common screens)
5. TODO: Multi-page wireframes
6. TODO: Sketch-to-wireframe (upload hand-drawn, AI refines)
