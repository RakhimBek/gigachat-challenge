import json

from pydantic import BaseModel

from storage_dao import insert_fact

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
    username: str
    message: str
    prev: list[str]
    next: list[str]


class Fact(BaseModel):
    text: str
    fact: str


class Facts(BaseModel):
    username: str
    facts: list[Fact]


def template(text):
    """example:
        Вытащи все факты о человеке по его сообщению.
        Верни результат как массив строк в JSON формате, в составе  обьекта с полем facts.
        Вот само сообщение:
            Я люблю ходить на рыбалку и сидеть там часами.
            Ещё у меня есть пес который тоже иногда ходит вместе со мной.
            Он любит бегать вокруг и исследовать местность.
            Иногда я паяю простые схемы, а так ещё мечтаю о собственном бизнесе, неком производстве
    """

    return HumanMessage(content=f"""
        Вытащи все факты о человеке по его сообщению.
        Верни каждый факт как массив объектов JSON, где ключ text - исходное сообщение, fact - факт.
        Вот само сообщение: {str(text)}
    """)


def ask_gigachat(userMessage):
    messages = []
    messages.append(userMessage.message)

    for m in userMessage.prev:
        messages.append(m)

    for m in userMessage.next:
        messages.append(m)

    answer = chat([
        SystemMessage(content=PRIMING_MESSAGE),
        template(' '.join(messages))
    ])

    facts = json.loads(answer.content)
    for v in facts:
        insert_fact(username=userMessage.username.lower(), text=v['text'], fact=v['fact'])

    return {
        "username": userMessage.username,
        "facts": facts
    }
