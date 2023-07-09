from typing import Union
from gpt import get_answer, model
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{ticket_id}")
def read_item(ticket_id: int, body: Union[str, None] = None):
    answer = get_answer(body)
    print(answer)
    json_compatible_data = jsonable_encoder(answer)
    answer_dict = {}
    answer_dict['answer'] = json_compatible_data
    final_answer = jsonable_encoder(answer_dict)
    return final_answer
