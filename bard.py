import http.client

print("Process 1")
conn = http.client.HTTPSConnection("bard-api-fast.p.rapidapi.com")
print("Process 2")
payload = "{\r\n    \"input_text\": \"Hey Bard\"\r\n}"
print("Process 3")
headers = {
    'content-type': "application/json",
    'X-RapidAPI-Key': "20734c03a9mshd72b89fbd6ea179p180777jsn99be2d020604",
    'X-RapidAPI-Host': "bard-api-fast.p.rapidapi.com"
}
print("Process 4")
conn.request("POST", "/get_answer?Secure_1PSID=awjHaAKuoonXdPqqzDWGgG1rb3aKdZbO3o8JZRrEMlmgoNJ2TOuUPUSGr6rTpHxJ5PganA.", payload, headers)
print("Process 5")
res = conn.getresponse()
print(res)
data = res.read()
print("Process 6")
print(data)
print(data.decode("utf-8"))
print(data.decode("utf-8")["answer"])