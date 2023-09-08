import speech_recognition as sr
import os
import webbrowser
import datetime
import win32com.client
import openai
from config import apikey
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# def bard(prom):


def Ai(prom):
    openai.api_key = apikey

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prom
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        var = response["choices"][0]["message"]["content"]
        say(response["choices"][0]["message"]["content"])
        print(f"Jarvis: {var}")
    except Exception as e:
        print("Some Error Occcured")
        say("Some Error Occured")


def say(text):
    speaker.Speak(text)


def takeCommand():
    print("Take Command Started...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occured. Sorry from Jarvis!"


if __name__ == '__main__':
    print('PyCharm')
    say("Hey Dj Whats going on")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com"],["javascript","https://www.youtube.com/watch?v=ER9SspLe4Hg&list=PLu0W_9lII9ahR1blWXxgSlL4y9iQBnLpR"],["google","https://www.google.com"],["flipkart","https://www.flipkart.com"],["boss","https://chat.openai.com/"],["instagram","https://www.instagram.com/"],["facebook","https://www.facebook.com/"],["gmail","https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"],["github","https://github.com/dhirajdj30"],["jio cinema","https://www.jiocinema.com/"],["only fans","https://onlyfans.com/"],["mini tv","https://www.amazon.in/minitv"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
        if "play music" in query.lower():
            musicPath = "C:/Users/91935/Downloads/Pink_blue.mp3"
            os.system(f"start {musicPath}")
        if "stop" in query.lower():
            say("Good Bye DJ")
            break
        if "the time" in query.lower():
            H = datetime.datetime.now().strftime("%H:%M")
            M = datetime.datetime.now().strftime("%H:%M")
            say(f"time is {H} baaj ke {M} minute")
        apps = [["vs code", "C:/Users\91935\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk"],
                 ["Python", "C:/ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm 2023.2.1.lnk"],
                 ["word", "C:/ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"],
                 ["power point", "C:/ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"],
                 ["chrome", "C:/ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"]]
        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                say(f"Starting {app[0]}")
                webbrowser.open(app[1])
        if "Ai mode".lower() in query.lower():
            say("A.I mode on. ")
            print("AI mode On")
            while True:
                print("Listening...")
                prom = takeCommand()
                print("")
                print(prom)
                if "Stop Ai".lower() in prom.lower():
                    say("Ai Stopped")
                    break
                if "Jarvis".lower() in prom.lower():
                    Ai(prom)
                else:
                    say("Error")


