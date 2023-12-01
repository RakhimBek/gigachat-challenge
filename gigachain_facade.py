from pydantic import BaseModel
from langchain.chat_models.gigachat import GigaChat

"""Пример работы с чатом через gigachain"""
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

from settings import GIGACHAT_CREDENTIAL
from settings import PRIMING_MESSAGE

# Авторизация в сервисе GigaChat
chat = GigaChat(
    credentials=GIGACHAT_CREDENTIAL,
    verify_ssl_certs=False
)


class Message(BaseModel):
    name: str
    message: str
    prev: list
    next: list


def template(text):
    return HumanMessage(content=f'Напиши все факты о человеке по его сообщению: {str(text)}')


def ask_gigachat(userMessage):
    messages = []
    messages.append(SystemMessage(content=PRIMING_MESSAGE))
    messages.append(template(userMessage.message))

    for m in userMessage.prev:
        messages.append(template(m))

    for m in userMessage.next:
        messages.append(template(m))

    answer = chat(messages)
    return {
        "name": userMessage.name,
        "facts": [answer]
    }
