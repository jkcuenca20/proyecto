from fastapi import FastAPI
import os
import httpx

app = FastAPI()
BACKEND_DATA = os.getenv("BACKEND_DATA_URL", "http://ms-data:80")

@app.get("/hello")
async def hello():
    # call backend-data
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            r = await client.get(f"{BACKEND_DATA}/hello")
            data = r.json()
    except Exception as e:
        data = {"error": str(e)}
    return {"message": "Hola desde API", "backend_data": data}

@app.get("/health")
def health():
    return {"status":"ok"}