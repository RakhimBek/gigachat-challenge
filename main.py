import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from settings import DEBUG
from settings import HOST
from settings import PORT
from settings import PROJECT_NAME

from dtos import Message
from gigachain_facade import ask_gigachat, ask_gigachat_as_is
from storage_dao import fetch_all_facts, fetch_all_facts_of_a_user
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
    return ({"message": "Go to /docs"})


@app.get("/api/chat")
async def root(system_message="", human_message="Who you are ?"):
    """
Сообщение чату AS IS для тестирования
    :param system_message: системное сообщение для чата. (некий прайминг задающий тенденцию/стратегию ответа модели, ее поведение)
    :param human_message: непосредственно анализируемое сообщение, промпт https://developers.sber.ru/help/gigachat/prompt-examples
    :return:
    """
    return ask_gigachat_as_is(system_message, human_message)


@app.get("/api/facts/all")
async def root():
    """
Список всех извлеченных аспектов/фактов
    :return: описание фактов (имя пользователя, исходной сообщение, факт)
    """
    return fetch_all_facts()


@app.get("/api/facts/search")
async def root(username):
    """
Список всех извлеченных фактов определенного пользователя
    :param username: имя пользователя
    :return: описание фактов (имя пользователя, исходной сообщение, факт)
    """
    return fetch_all_facts_of_a_user(username)


@app.post("/api/ask")
async def ask(message: Message):
    """
Запрос фактов по сообщению пользователя
    :param message: описание сообщения
    :return: описание фактов (имя пользователя, исходной сообщение, факт)
    """
    return ask_gigachat(message)


@app.post("/api/ask/all")
async def ask_all(messages: list[Message]):
    """
Запрос фактов по несольким сообщениям пользователей
    :param messages: коллекция сообщений пользователей
    :return: коллекция описании фактов (имя пользователя, исходной сообщение, факт)
    """
    return [ask_gigachat(message) for message in messages]


if __name__ == '__main__':
    init_database()
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
