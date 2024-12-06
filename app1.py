from fastapi import FastAPI
from fastapi import Header
from pydantic import BaseModel
from typing import Optional

class Computer(BaseModel):
    computerid: int
    cpu: Optional[str]
    gpu: Optional[str]
    price: float
    





app = FastAPI(
    title="My API",
    description="My own API powered by FastAPI.",
    version="1.0.1")


app.put('/computer',name='create a new computerr')
def get_computer(computer: Computer):
    """Essaye de créer un computer dans la base de données"""
    return computer



@app.get('/')
def get_index():
    """Returns greetings
    """
    return {'greetings': 'welcome'}






