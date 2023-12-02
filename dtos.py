from pydantic import BaseModel


class Message(BaseModel):
    username: str
    message: str
    prev: list[str]
    next: list[str]


class Fact(BaseModel):
    username: str
    text: str
    fact: str


class Facts(BaseModel):
    username: str
    facts: list[Fact]
