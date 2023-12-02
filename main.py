import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from settings import DEBUG
from settings import HOST
from settings import PORT
from settings import PROJECT_NAME

from gigachain_facade import Message
from gigachain_facade import ask_gigachat

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
    return {"message": "Hello World"}


@app.post("/api/ask")
async def ask(message: Message):
    return ask_gigachat(message)


if __name__ == '__main__':
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
