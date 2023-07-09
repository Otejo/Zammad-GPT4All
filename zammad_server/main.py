from typing import Union
import os
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import http
import json
import requests
from urllib.parse import urlencode

#enter server address for gpt4all
gpt4all_address = "x.x.x.x:8000"
zammad_address = "x.x.x.x"
zammad_secret = os.environ.get("zammad_password")
zammad_email = 'admin_email@forZammad.com'
zammad_auth = (zammad_email, zammad_secret)
app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

#remove HTML formatting to make it easier for GPT4All
def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
        

#send email to GPT4all
def update_ticket(ticket_id, subject, body):
    payload = {
        "ticket_id": ticket_id,
        "subject": subject,
        "body": body,
        "content_type": "text/html",
        "type": "email",
        "internal": "True",
        "Sender": "Agent",
        "time_unit": "15"
    }
    url = zammad_address+'/api/v1/ticket_articles'
    r = requests.post(url,auth=zammad_auth, data=payload)
    print(r)



@app.post("/ticket", status_code=http.HTTPStatus.ACCEPTED)
async def webhook(request: Request):
    payload = await request.body()
    print(payload)
    data = json.loads(payload)
    ticket_id = data.get("ticket_id")
    subject = data.get("subject")
    body = data.get("article_body")
    bodyforsend = {'body':(remove_html_tags(body))}
    url = gpt4all_address+'/items/'+str(ticket_id)
    r = requests.get(url, bodyforsend)
    response_from_chat = r.json()
    answer = response_from_chat.get('answer')
    #article_type = data.get("type")
    print(answer)
    update_ticket(ticket_id, subject, answer)
    print(zammad_auth)
    return {}

    
    