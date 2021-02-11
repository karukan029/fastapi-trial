from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# @app.get('/') # methodとendpointの指定
# async def hello():
#     return {"text": "hello world!"}

@app.get('/get/{path}')
async def path_and_query_params(
        path: str,
        query: int,
        default_none: Optional[str] = None):
    return {"text":f"hello,{path}, {query} and {default_none}"}

class ItemOut(BaseModel):
    strings: str
    aux: int = 1
    text: str

@app.get('/', response_model=ItemOut)
async def response(strings: str, integer: int):
    return {"text": "hello world!", "strings": strings, "integer": integer}