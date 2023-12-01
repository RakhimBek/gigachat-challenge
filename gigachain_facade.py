from pydantic import BaseModel


class Message(BaseModel):
    name: str
    message: str


def ask_gigachat(message):
    return {
        "name": message.name,
        "facts": ["любит собак", "бегает", "играет в шахматы"]
    }
