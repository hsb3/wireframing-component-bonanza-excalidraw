# Wireframe Copilot - System Diagram

## Legend
- ✅ **Implemented** - Code exists, needs testing
- ⏳ **Partial** - Scaffolding exists, needs completion
- ❌ **Not Started** - Needs to be built

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          USER BROWSER                               │
│  http://localhost:8000/app                                          │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              │ HTTP requests
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     FASTAPI SERVER ✅                                │
│                   (backend/src/agent/app.py)                        │
│                                                                     │
│  • GET  /health          → Health check                            │
│  • GET  /app/*           → Serve React static files                │
│  • POST /threads         → LangGraph: Create conversation          │
│  • POST /runs/stream     → LangGraph: Stream agent responses       │
│                                                                     │
│  Port: 8000                                                         │
└─────────────────────────────────────────────────────────────────────┘
         │                                    │
         │ Serves static files                │ Routes to LangGraph
         ▼                                    ▼
┌──────────────────────┐      ┌────────────────────────────────────────┐
│  REACT APP ⏳         │      │  LANGGRAPH DEEP AGENT ⏳                │
│  (frontend/dist/)    │      │  (backend/src/agent/graph.py)          │
│                      │      │                                        │
│  Status: Built but   │      │  Status: Scaffolded, needs completion  │
│  needs npm install + │      │                                        │
│  npm run build       │      │  Model: Claude Sonnet 4.5 ✅           │
│                      │      │  Framework: LangGraph ✅               │
└──────────────────────┘      │  Tools: 4 defined ✅                   │
                              │  Integration: Needs testing ❌          │
                              └────────────────────────────────────────┘
                                              │
                                              │ Uses tools
                                              ▼
                              ┌────────────────────────────────────────┐
                              │       AGENT TOOLS                      │
                              │                                        │
                              │  1. search_components ✅               │
                              │     - Searches registry                │
                              │     - Returns matches                  │
                              │                                        │
                              │  2. get_component ✅                   │
                              │     - Gets full metadata               │
                              │                                        │
                              │  3. list_categories ✅                 │
                              │     - Browse categories                │
                              │                                        │
                              │  4. compose_wireframe ⏳               │
                              │     - Loads components                 │
                              │     - Composes .excalidraw             │
                              │     - Needs testing ❌                 │
                              └────────────────────────────────────────┘
                                              │
                                              │ Reads from
                                              ▼
```

---

## Frontend Layer (Detailed)

```
┌─────────────────────────────────────────────────────────────────────┐
│                         REACT FRONTEND ⏳                            │
│                    (frontend/src/)                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  APP SHELL ✅                                                 │ │
│  │  (App.tsx)                                                    │ │
│  │                                                               │ │
│  │  • Header with title                                         │ │
│  │  • Toggle copilot button                                     │ │
│  │  • Responsive layout                                         │ │
│  │                                                               │ │
│  │  Status: Component exists, needs polish                      │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌─────────────────────┐         ┌──────────────────────────────┐ │
│  │  COPILOT PANEL ⏳   │         │  EXCALIDRAW CANVAS ✅         │ │
│  │  (CopilotPanel.tsx) │         │  (@excalidraw/excalidraw)    │ │
│  │                     │         │                              │ │
│  │  • Chat messages ✅ │         │  • Full Excalidraw editor ✅ │ │
│  │  • Input box ✅     │         │  • API integration ✅        │ │
│  │  • Send button ✅   │         │  • Scene updates ⏳          │ │
│  │  • Tool calls ⏳    │         │                              │ │
│  │  • Streaming ⏳     │         │  Status: Embedded, needs     │ │
│  │                     │         │  wire-up for generated       │ │
│  │  Status: UI done,   │         │  wireframes                  │ │
│  │  needs LangGraph    │         └──────────────────────────────┘ │
│  │  SDK integration ❌ │                                           │
│  └─────────────────────┘                                           │
│            │                                                        │
│            └──── Uses LangGraph SDK (@langchain/langgraph-sdk) ❌  │
│                  Needs: npm install                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Backend Layer (Detailed)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    LANGGRAPH BACKEND ⏳                              │
│                  (backend/src/agent/)                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  DEEP AGENT ⏳                                                │ │
│  │  (graph.py)                                                   │ │
│  │                                                               │ │
│  │  Components:                                                  │ │
│  │  • create_deep_agent() ✅                                     │ │
│  │  • Claude Sonnet 4.5 LLM ✅                                   │ │
│  │  • System prompt with catalog ✅                              │ │
│  │  • 4 tools registered ✅                                      │ │
│  │                                                               │ │
│  │  Status: Graph defined, needs LangGraph CLI testing ❌        │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                              │                                      │
│                              │ Uses                                 │
│                              ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  TOOLS IMPLEMENTATION                                         │ │
│  │                                                               │ │
│  │  1. search_components(query, theme, limit) ✅                │ │
│  │     - Code: Complete                                         │ │
│  │     - Tests: None ❌                                          │ │
│  │                                                               │ │
│  │  2. get_component(component_id) ✅                            │ │
│  │     - Code: Complete                                         │ │
│  │     - Tests: None ❌                                          │ │
│  │                                                               │ │
│  │  3. list_categories(theme) ✅                                │ │
│  │     - Code: Complete                                         │ │
│  │     - Tests: None ❌                                          │ │
│  │                                                               │ │
│  │  4. compose_wireframe(name, theme, components) ⏳            │ │
│  │     - Code: Scaffold exists                                  │ │
│  │     - Needs: Complete composer.py implementation ❌          │ │
│  │     - Needs: Testing ❌                                       │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                              │                                      │
│                              │ Reads from                           │
│                              ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  WIREFRAME COMPOSER ⏳                                        │ │
│  │  (backend/src/tools/composer.py)                             │ │
│  │                                                               │ │
│  │  • WireframeComposer class ✅                                │ │
│  │  • compose() method ✅                                        │ │
│  │  • _load_component_elements() ✅                             │ │
│  │  • Library file caching ✅                                    │ │
│  │                                                               │ │
│  │  Status: Code written, needs debugging/testing ❌            │ │
│  └──────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Data Layer (Detailed)

```
┌─────────────────────────────────────────────────────────────────────┐
│                         DATA LAYER                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  COMPONENT REGISTRY ✅                                        │ │
│  │  (backend/src/data/component-registry.json)                  │ │
│  │                                                               │ │
│  │  • 1,078 components indexed                                  │ │
│  │  • 7 themes (includes old names)                             │ │
│  │  • 46 categories                                             │ │
│  │  • Searchable by: name, tags, category                       │ │
│  │                                                               │ │
│  │  Generated by: scripts/generate_component_registry.py ✅     │ │
│  │  Status: Complete and populated ✅                            │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                              │                                      │
│                              │ References                           │
│                              ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  COMPONENT LIBRARIES ✅                                       │ │
│  │  (../../output/)                                             │ │
│  │                                                               │ │
│  │  • mork-wireframe-kit.excalidrawlib (154 components)         │ │
│  │  • abc123-dark-wireframe-kit.excalidrawlib (154 components)  │ │
│  │  • bronzer-wireframe-kit.excalidrawlib (154 components)      │ │
│  │  • Legacy: default, carbon, warm, shadcn-saas-kit            │ │
│  │                                                               │ │
│  │  Status: Generated and available ✅                           │ │
│  │  Location: Filesystem accessible by backend ✅                │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  COMPONENT CATALOG ✅                                         │ │
│  │  (backend/src/data/component-catalog.txt)                    │ │
│  │                                                               │ │
│  │  • Human-readable component list                             │ │
│  │  • Used in agent system prompt                               │ │
│  │  • Organized by theme and category                           │ │
│  │                                                               │ │
│  │  Status: Auto-generated ✅                                    │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  OUTPUT WIREFRAMES ❌                                         │ │
│  │  (wireframes/)                                               │ │
│  │                                                               │ │
│  │  • .excalidraw files generated by agent                      │ │
│  │  • Loaded into canvas for viewing                            │ │
│  │                                                               │ │
│  │  Status: Folder exists, no files yet ❌                       │ │
│  └──────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Complete System Map with Status

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                                USER WORKFLOW                                   │
│                                                                                │
│  1. Open browser → http://localhost:8000/app                                  │
│  2. Type in copilot: "Create a login screen"                                  │
│  3. See wireframe appear on Excalidraw canvas                                 │
│  4. Iterate: "Add logo at top"                                                │
│  5. Export or share                                                           │
└────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌────────────────────────────────────────────────────────────────────────────────┐
│                              FRONTEND (React) ⏳                                │
│                              Port: 5173 (dev) or served from 8000 (prod)      │
├────────────────────────────────────────────────────────────────────────────────┤
│                                                                                │
│  ┌─────────────────────┐  ┌─────────────────────┐  ┌────────────────────────┐│
│  │  App Shell ✅        │  │  Copilot Panel ⏳    │  │  Excalidraw Canvas ✅  ││
│  │  (App.tsx)          │  │  (CopilotPanel.tsx) │  │  (@excalidraw/         ││
│  │                     │  │                     │  │   excalidraw)          ││
│  │  • Header ✅         │  │  • Messages ✅       │  │                        ││
│  │  • Layout ✅         │  │  • Input ✅          │  │  • Embedded ✅          ││
│  │  • Toggle button ✅  │  │  • Send ✅           │  │  • API ref ✅           ││
│  │                     │  │  • Streaming ❌      │  │  • Update scene ❌      ││
│  │  NEEDS:             │  │  • Tool calls ❌     │  │  • Load wireframe ❌    ││
│  │  • Polish           │  │                     │  │                        ││
│  │                     │  │  NEEDS:             │  │  NEEDS:                ││
│  │                     │  │  • SDK integration  │  │  • Wire up generated   ││
│  │                     │  │  • Stream handling  │  │    wireframes          ││
│  │                     │  │  • Error handling   │  │  • Test with agent     ││
│  └─────────────────────┘  └─────────────────────┘  └────────────────────────┘│
│                                      │                          ▲              │
│                                      │ HTTP/SSE                 │              │
│                                      │ LangGraph API            │              │
│                                      │                          │              │
│                                      └──────────────────────────┘              │
│                                         Updates canvas with                    │
│                                         generated wireframes                   │
│                                                                                │
│  BUILD STATUS:                                                                 │
│  • npm install ❌ (not run yet)                                                │
│  • npm run build ❌ (not built yet)                                            │
│  • TypeScript compilation ❌                                                   │
│                                                                                │
└────────────────────────────────────────────────────────────────────────────────┘
```

---

## Backend Layer (Detailed)

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                         BACKEND (Python) ⏳                                     │
│                         Port: 8000                                             │
├────────────────────────────────────────────────────────────────────────────────┤
│                                                                                │
│  ┌──────────────────────────────────────────────────────────────────────────┐ │
│  │  FASTAPI APP ✅                                                           │ │
│  │  (src/agent/app.py)                                                      │ │
│  │                                                                          │ │
│  │  Routes:                                                                 │ │
│  │  • GET  /health              ✅ Health check                            │ │
│  │  • GET  /app/*               ✅ Serve React files                       │ │
│  │  • (LangGraph routes)        ⏳ Auto-mounted by LangGraph server        │ │
│  │                                                                          │ │
│  │  NEEDS:                                                                  │ │
│  │  • Test with `langgraph dev` ❌                                          │ │
│  │  • Verify static file serving ❌                                         │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
│                                                                                │
│  ┌──────────────────────────────────────────────────────────────────────────┐ │
│  │  LANGGRAPH AGENT ⏳                                                       │ │
│  │  (src/agent/graph.py)                                                    │ │
│  │                                                                          │ │
│  │  Configuration:                                                          │ │
│  │  • Model: ChatAnthropic ✅                                               │ │
│  │  • Model ID: claude-sonnet-4-5-20250929 ✅                               │ │
│  │  • Temperature: 0 ✅                                                      │ │
│  │  • System message: With component catalog ✅                             │ │
│  │  • Tools: 4 defined ✅                                                    │ │
│  │  • State: AgentState TypedDict ✅                                        │ │
│  │  • Graph: create_deep_agent ✅                                           │ │
│  │                                                                          │ │
│  │  NEEDS:                                                                  │ │
│  │  • Environment variables (.env with ANTHROPIC_API_KEY) ❌                │ │
│  │  • Test graph execution ❌                                                │ │
│  │  • Verify tool calling works ❌                                          │ │
│  │  • Debug any LangGraph errors ❌                                         │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
│                                                                                │
│  ┌──────────────────────────────────────────────────────────────────────────┐ │
│  │  WIREFRAME COMPOSER ⏳                                                    │ │
│  │  (src/tools/composer.py)                                                 │ │
│  │                                                                          │ │
│  │  • WireframeComposer class ✅                                            │ │
│  │  • compose() method ✅                                                    │ │
│  │  • _get_component_by_id() ✅                                             │ │
│  │  • _load_component_elements() ✅                                         │ │
│  │  • Library caching ✅                                                     │ │
│  │                                                                          │ │
│  │  NEEDS:                                                                  │ │
│  │  • Test component loading from .excalidrawlib ❌                         │ │
│  │  • Verify element ID generation ❌                                       │ │
│  │  • Test position translation ❌                                          │ │
│  │  • Handle missing components gracefully ❌                               │ │
│  │  • Add __init__.py files for imports ❌                                  │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
│                                                                                │
│  DEPENDENCIES STATUS:                                                          │
│  • pyproject.toml created ✅                                                   │
│  • uv pip install -e . ❌ (not run yet)                                        │
│  • langgraph CLI ❌ (needs installation)                                       │
│                                                                                │
└────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      │ Reads from filesystem
                                      ▼
┌────────────────────────────────────────────────────────────────────────────────┐
│                          DATA LAYER (Files) ✅                                  │
├────────────────────────────────────────────────────────────────────────────────┤
│                                                                                │
│  Location: /Users/henry/Desktop/shadcn-excalidraw/                            │
│                                                                                │
│  ┌──────────────────────────────────────────────────────────────────────────┐ │
│  │  COMPONENT LIBRARIES ✅                                                   │ │
│  │  (output/*.excalidrawlib)                                                │ │
│  │                                                                          │ │
│  │  • mork-wireframe-kit.excalidrawlib ✅                                   │ │
│  │  • abc123-dark-wireframe-kit.excalidrawlib ✅                            │ │
│  │  • bronzer-wireframe-kit.excalidrawlib ✅                                │ │
│  │  • 154 components each                                                   │ │
│  │  • Themes applied, visibility fixed                                      │ │
│  │  • Frames scaled correctly                                               │ │
│  │                                                                          │ │
│  │  Status: Ready to use ✅                                                  │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
│                                                                                │
│  ┌──────────────────────────────────────────────────────────────────────────┐ │
│  │  COMPONENT REGISTRY ✅                                                    │ │
│  │  (wireframing-solution/backend/src/data/component-registry.json)        │ │
│  │                                                                          │ │
│  │  • Auto-generated from libraries ✅                                      │ │
│  │  • 1078 components with metadata                                         │ │
│  │  • Includes dimensions, tags, descriptions                               │ │
│  │  • Maps to library file + index                                          │ │
│  │                                                                          │ │
│  │  Status: Generated and available ✅                                       │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
│                                                                                │
│  ┌──────────────────────────────────────────────────────────────────────────┐ │
│  │  COMPONENT CATALOG ✅                                                     │ │
│  │  (wireframing-solution/backend/src/data/component-catalog.txt)          │ │
│  │                                                                          │ │
│  │  • Human-readable component list                                         │ │
│  │  • Included in agent system prompt                                       │ │
│  │  • Organized by theme and category                                       │ │
│  │                                                                          │ │
│  │  Status: Generated ✅                                                     │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────────────┘
```

---

## Integration Points & Status

```
┌────────────────────────────────────────────────────────────────────┐
│                    INTEGRATION POINTS                              │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  1. Frontend ←→ Backend Communication                              │
│     Status: ⏳ Partial                                              │
│     • LangGraph SDK imported ✅                                     │
│     • Client.runs.stream() implemented ✅                           │
│     • Need to test end-to-end ❌                                    │
│                                                                    │
│  2. Agent ←→ Component Libraries                                   │
│     Status: ✅ Implemented                                          │
│     • Registry JSON loaded in graph.py ✅                           │
│     • Composer reads .excalidrawlib files ✅                        │
│     • File paths configured correctly ✅                            │
│                                                                    │
│  3. Composer ←→ Excalidraw Canvas                                  │
│     Status: ❌ Not Connected                                        │
│     • Composer saves .excalidraw files ✅                           │
│     • Canvas can load .excalidraw ✅ (Excalidraw feature)          │
│     • Frontend needs to load generated files ❌                     │
│     • Need file endpoint or direct JSON passing ❌                  │
│                                                                    │
│  4. LangGraph ←→ FastAPI                                           │
│     Status: ⏳ Configured but untested                              │
│     • langgraph.json configured ✅                                  │
│     • Graph and app paths defined ✅                                │
│     • Need to run `langgraph dev` to test ❌                        │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## Dependency Installation Status

```
┌────────────────────────────────────────────────────────────────────┐
│                    DEPENDENCIES                                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  BACKEND:                                                          │
│  • pyproject.toml created ✅                                        │
│  • langgraph ❌ (needs: uv add langgraph)                          │
│  • langchain-anthropic ❌ (needs: uv add langchain-anthropic)      │
│  • fastapi ❌ (needs: uv add fastapi)                              │
│  • uvicorn ❌ (needs: uv add uvicorn)                              │
│  • pillow ❌ (needs: uv add pillow)                                │
│  • LangGraph CLI ❌ (needs: pip install langgraph-cli)             │
│                                                                    │
│  FRONTEND:                                                         │
│  • package.json created ✅                                          │
│  • node_modules ❌ (needs: npm install)                            │
│  • react ❌                                                         │
│  • @excalidraw/excalidraw ❌                                        │
│  • @langchain/langgraph-sdk ❌                                      │
│  • vite ❌                                                          │
│  • tailwindcss ❌                                                   │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## Next Steps Checklist

### Backend (2-3 hours)
- [ ] `cd wireframing-solution/backend`
- [ ] `uv pip install -e .` - Install Python dependencies
- [ ] Create `.env` file with `ANTHROPIC_API_KEY`
- [ ] Add missing `__init__.py` files for imports
- [ ] Test: `python scripts/generate_component_registry.py` (already done ✓)
- [ ] Test: `langgraph dev` - Start server
- [ ] Debug any import errors
- [ ] Test health endpoint: `curl http://localhost:8000/health`

### Frontend (1-2 hours)
- [ ] `cd wireframing-solution/frontend`
- [ ] `npm install` - Install Node dependencies
- [ ] Fix any TypeScript errors
- [ ] Test: `npm run dev` - Start dev server
- [ ] Open http://localhost:5173
- [ ] Debug any build errors

### Integration (2-3 hours)
- [ ] Start backend: `langgraph dev` (port 8000)
- [ ] Test LangGraph API: Create thread, send message
- [ ] Start frontend: `npm run dev` (port 5173)
- [ ] Test chat → backend communication
- [ ] Debug CORS if needed (shouldn't be needed with proxy)
- [ ] Wire up Excalidraw canvas updates
- [ ] Test end-to-end: type in chat → see wireframe

### Production Build (30 min)
- [ ] `cd frontend && npm run build`
- [ ] Restart backend to serve built files
- [ ] Access at http://localhost:8000/app
- [ ] Verify all features work in production mode

---

## Critical Path Items ❌

**These MUST be completed for MVP:**

1. **Install dependencies** (backend + frontend)
2. **Add `__init__.py` files** to Python packages
3. **Create `.env`** with API keys
4. **Test LangGraph agent** locally
5. **Fix imports** in backend
6. **Wire up canvas updates** in frontend
7. **Test compose_wireframe** tool with real libraries

**Estimated time:** 4-6 hours for a developer familiar with the stack

---

## System Health Checklist

When everything is working, you should see:

### Backend
```bash
$ langgraph dev
✓ Server running on http://localhost:8000
✓ Graph 'agent' loaded successfully
✓ 4 tools registered
✓ Component registry loaded (1078 components)
```

### Frontend
```bash
$ npm run dev
✓ Vite dev server running on http://localhost:5173
✓ React app compiled
✓ No TypeScript errors
```

### Integration
```bash
$ curl http://localhost:8000/health
{"status":"healthy","service":"wireframe-agent","version":"0.1.0"}

$ curl http://localhost:8000/app
<!DOCTYPE html>... (React app HTML)
```

### Usage
- Type in copilot: "Create a button"
- Agent calls search_components
- Agent calls compose_wireframe
- Wireframe appears on canvas
- File saved to wireframes/button.excalidraw

---

## Summary

**What's ✅ DONE:**
- Complete file structure
- All source code scaffolded
- Component registry generated (1078 components)
- LangGraph agent defined
- React app shell built
- Copilot UI created
- Composer logic written

**What's ❌ NOT DONE:**
- Dependencies not installed
- Code not tested
- Integration not verified
- Missing __init__.py files
- No .env file created
- Canvas updates not wired
- End-to-end flow not tested

**Time to complete:** 4-6 hours for an experienced developer
**Next action:** Install dependencies and test each layer
