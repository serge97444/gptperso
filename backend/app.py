from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Dict
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
#from utils.llm_agent import run_agent,load_models

app = FastAPI(title="Demo app", version = "0.1",description="An agent API to send me stock messages")

origins = ["http://localhost:8080","http://localhost:3000","http://localhost:80"]

app.add_middleware(CORSMiddleware,
                   allow_origins= origins,
                   allow_methods=["*"])

class Message(BaseModel):
    message:str

#llm, tokenizer = load_models()

@app.get('/infos',tags = ['infos'])
def infos():
    return "hello from demo app"

# @app.post("/chat")
# async def chat(message : Message):
#     print('received message : ' , message)
#     response = await run_agent(message.message , llm=llm, tokenizer=tokenizer)
#     #sources = ["A","B"]
#     print('response : ' , response)
#     print('query : ' , message.message)
#     response_content = {"query":message.message ,  "response" : response}
#     return JSONResponse(content=response_content, status_code=200)