from fastapi import FastAPI

from utils import get_response

app = FastAPI()

@app.get("/chatbot")
async def chatbot(question:str):
    res=get_response(question)
    return res
