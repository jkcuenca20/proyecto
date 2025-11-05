from fastapi import FastAPI
import os

app = FastAPI()
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "commentsdb")
DB_USER = os.getenv("DB_USER", "user")

@app.get("/hello")
def hello():
    # Simula consulta a DB (por ejemplo)
    return {"message": "Hola desde Data", "db_host": DB_HOST, "db_name": DB_NAME, "db_user": DB_USER}

@app.get("/health")
def health():
    return {"status":"ok"}