"""
FastAPI app for serving the React frontend and health checks
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI(
    title="Wireframe Agent API",
    description="AI-powered wireframe generation using LangGraph"
)

# Health check endpoint
@app.get("/health")
async def health():
    """Health check for deployment"""
    return {
        "status": "healthy",
        "service": "wireframe-agent",
        "version": "0.1.0"
    }

# Serve React frontend
frontend_dir = Path(__file__).parent.parent.parent.parent / "frontend" / "dist"

if frontend_dir.exists():
    # Serve static files
    app.mount("/assets", StaticFiles(directory=frontend_dir / "assets"), name="assets")

    # Serve index.html for all other routes (SPA)
    @app.get("/app/{full_path:path}")
    async def serve_frontend(full_path: str):
        """Serve React app"""
        index_file = frontend_dir / "index.html"
        if index_file.exists():
            return FileResponse(index_file)
        return {"error": "Frontend not built. Run: cd frontend && npm run build"}

    @app.get("/app")
    async def serve_frontend_root():
        """Serve React app root"""
        index_file = frontend_dir / "index.html"
        if index_file.exists():
            return FileResponse(index_file)
        return {"error": "Frontend not built. Run: cd frontend && npm run build"}
else:
    @app.get("/app")
    async def frontend_not_built():
        return {
            "error": "Frontend not built yet",
            "instructions": "Run: cd frontend && npm install && npm run build"
        }

# LangGraph API will be automatically mounted at /threads, /runs, etc.
# by the LangGraph server when deployed
