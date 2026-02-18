import { useState, useCallback } from 'react'
import { Excalidraw } from '@excalidraw/excalidraw'
import CopilotPanel from './components/CopilotPanel'
import './App.css'

function App() {
  const [excalidrawAPI, setExcalidrawAPI] = useState<any>(null)
  const [copilotOpen, setCopilotOpen] = useState(true)

  const handleExcalidrawAPI = useCallback((api: any) => {
    setExcalidrawAPI(api)
  }, [])

  const handleWireframeGenerated = useCallback((excalidrawData: any) => {
    // Update Excalidraw canvas with generated wireframe
    if (excalidrawAPI) {
      excalidrawAPI.updateScene(excalidrawData)
    }
  }, [excalidrawAPI])

  return (
    <div className="app-container">
      {/* Header */}
      <header className="app-header">
        <h1>Wireframe Copilot</h1>
        <button
          onClick={() => setCopilotOpen(!copilotOpen)}
          className="toggle-copilot"
        >
          {copilotOpen ? 'Hide' : 'Show'} Copilot
        </button>
      </header>

      {/* Main content */}
      <div className="app-content">
        {/* Copilot sidebar */}
        {copilotOpen && (
          <aside className="copilot-sidebar">
            <CopilotPanel
              onWireframeGenerated={handleWireframeGenerated}
              excalidrawAPI={excalidrawAPI}
            />
          </aside>
        )}

        {/* Excalidraw canvas */}
        <main className="canvas-container">
          <Excalidraw
            excalidrawAPI={handleExcalidrawAPI}
            initialData={{
              appState: {
                viewBackgroundColor: "#ffffff",
                currentItemStrokeColor: "#000000",
              }
            }}
          />
        </main>
      </div>
    </div>
  )
}

export default App
