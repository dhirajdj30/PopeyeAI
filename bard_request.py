import requests
from main import say, takeCommand

def Bard(prom):
    url = "https://bard-api-fast.p.rapidapi.com/get_answer"

    querystring = {"Secure_1PSID":"<REQUIRED>"}

    payload = {"input_text": prom}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "<REQUIRED>",
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

