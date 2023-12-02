import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from settings import DEBUG
from settings import HOST
from settings import PORT
from settings import PROJECT_NAME

from gigachain_facade import Message
from gigachain_facade import ask_gigachat
from storage_dao import fetch_all_facts
from storage_initializer import init_database

app = FastAPI(
    title=PROJECT_NAME,
    debug=DEBUG,
    version='1.0',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return ({"message": "Hello World"})


@app.get("/api/facts/all")
async def root():
    return fetch_all_facts()


@app.post("/api/ask")
async def ask(message: Message):
    return ask_gigachat(message)


@app.post("/api/ask/all")
async def ask_all(messages: list[Message]):
    return [ask_gigachat(message) for message in messages]


if __name__ == '__main__':
    init_database()
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
