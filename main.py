# File: main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Render GPT6 CONTINUE!"}

@app.get("/add")
def add(a: int, b: int):
   return {"result": a + b}
