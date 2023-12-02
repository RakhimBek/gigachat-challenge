import json
import yaml

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
        Формат ответа YAML
        Выведи только существующиме факты из жизни автора, личность, желания, хобби, увлечения, характеристики следующие из его сообщения    
        Вот само сообщение: {str(text)}
    """)


def ask_gigachat(userMessage):
    messages = []
    messages.append(userMessage.message)

    for m in userMessage.prev:
        messages.append(m)

    for m in userMessage.next:
        messages.append(m)

    joined_content = ' '.join(messages)
    answer = chat([
        SystemMessage(content=PRIMING_MESSAGE),
        template(joined_content)
    ])

    try:
        content_yaml = answer.content

        content_object = yaml.safe_load(content_yaml)

        facts = {}
        for entry in content_object:
            row = dict(entry)
            for key in row.keys():
                value = row[key]
                insert_fact(username=userMessage.username.lower(), text=joined_content, fact=value)
                facts[key] = value

        return {
            "username": userMessage.username,
            "facts": facts
        }
    except Exception as e:
        print(f'request: {joined_content}')
        print(f'answer: {answer.content}')
        print(e)
        return {
            "username": userMessage.username,
            "facts": []
        }
