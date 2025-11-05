from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import httpx
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

BACKEND_API = os.getenv("BACKEND_API_URL", "http://ms-api:80")

@app.get("/api/hello")
async def call_api():
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            r = await client.get(f"{BACKEND_API}/hello")
            return JSONResponse(content=r.json())
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Serve index at root
@app.get("/")
def index():
    return {"message": "Front ready. Try /api/hello"}
