from fastapi import FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database.database import get_db

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}