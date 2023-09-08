import requests
from main import say, takeCommand

def Bard(prom):
    url = "https://bard-api-fast.p.rapidapi.com/get_answer"

    querystring = {"Secure_1PSID":"awjHaNGge7DhFSUjfIVG8mDq6hmgNwEBsrfydO9PATBeUg5YdLbKiVzKd1J687AqjRRdcg."}

    payload = {"input_text": prom}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "20734c03a9mshd72b89fbd6ea179p180777jsn99be2d020604",
        "X-RapidAPI-Host": "bard-api-fast.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers, params=querystring)
    print(response.json())
    say(response.json()["answer"])
    print(response.json()["answer"])


say("Hey DJ! Bard is Here to help you!")
while True:
    print('Lisenting...')
    query = takeCommand()
    if "stop".lower() in query.lower():
        break
    else:
        prom = takeCommand()
        Bard(prom)

