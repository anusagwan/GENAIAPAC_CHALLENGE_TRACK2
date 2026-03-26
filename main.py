from fastapi import FastAPI
from fastapi.responses import FileResponse
from agent.agent import run_agent

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/ask")
def ask(query: str):
    response = run_agent(query)
    return {"response": response}