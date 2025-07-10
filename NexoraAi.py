                        #Nexora AI Beta Version


#Imported Modules

import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as pt
import music_lib 
from gtts import gTTS
import pygame
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import pyautogui as pyt
import time
import subprocess as sb
import commands as cmd
import datetime as dt
import google.generativeai as genai
import psutil as ps
import json
import questions

#Shutdown function

def shutdown():   
     os.system("shutdown /s /f /t 0") 

#TTS

def speak(text):  
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

#Date Checker

def check_date():
    birthdate= "YOUR_BIRTHDATE_HERE"
    today = dt.datetime.now().strftime("%Y-%m-%d")
    if birthdate == today:
        speak("Happy Birthday YOUR_NAME")

        messagebox.showinfo("Birthday","Happy Birthday to you YOUR_NAME!")
        speak("Happy Birthday YOUR_NAME")
    else:
        speak(f"Today is {today}!")

#Time checker

def get_time():
    current_time = dt.datetime.now().strftime("%H:%M:%S")
    if current_time == "22:00:00":
        speak(f"{name} I request you to wrap up your work as the system will shut in 1 minute because the time is 10 PM")
        time.sleep(60)
        speak("Shutting Down")
        shutdown()
    else:
        return f"The current time is {current_time}"
    
#Question Answer

def ask_question():
    speak("Opening Nexora AI Chatbot")
    speak("Sir ask your query here")
    API_KEY = "YOUR_API_KEY"
    genai.configure(api_key=API_KEY)

    model=genai.GenerativeModel("gemini-2.0-flash")

    chat = model.start_chat()

    print("Chat with Nexora! Type exit to quit")
    while True:
        user_input=input("You:")
        if user_input in questions.nexora_knowledge:
            answer=questions.nexora_knowledge[user_input]
            print("Nexora:",answer)
        elif user_input.lower()=='exit':
            break
        else:
            response = chat.send_message(user_input)
            summarizer = genai.GenerativeModel("gemini-1.5-flash")
            summary = summarizer.generate_content(f"Summarize this in 2-3 lines like you're speaking: {response.text}")
            print("Nexora:",summary)

#Uptime Checker

start_time= time.time() 

def get_uptime():
    elapsed_time = time.time() - start_time
    hours = elapsed_time // 3600
    minutes = (elapsed_time % 3600) // 60
    seconds = elapsed_time % 60
    return f"System has been running for {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds."

  

recognizer = sr.Recognizer()
engine = pt.init()

#Mathematician

def mathematics():
    root= tk.Tk()
    root.withdraw()
    operation = simpledialog.askstring("Nexora AI","Which operation you want to do??")
    if operation == "Addition":
        num = simpledialog.askinteger("Nexora AI","Enter the 1st number")
        num2 = simpledialog.askinteger("Nexora AI","Enter the 2nd number")
        sum = num + num2
        messagebox.showinfo("Nexora AI",f"The sum of {num} and {num2} is {sum}")
    elif operation == "Subtraction":
        sss = simpledialog.askinteger("Nexora AI","Enter the 1st number(greater)")
        ss = simpledialog.askinteger("Nexora AI","Enter the 2nd number")
        difference = sss - ss
        messagebox.showinfo("Nexora AI",f"The difference of {sss} and {ss} is {difference}")
    elif operation == "Division":
        dici = simpledialog.askinteger("Nexora AI","Enter the 1st number(greater)")
        divi = simpledialog.askinteger("Nexora AI","Enter the 2nd number from the number will be divided")
        quotient = dici/divi
        messagebox.showinfo("Nexora AI",f"The quotient of {dici} and {divi} is {quotient}")
    elif operation == "Multiplication":
        mmm= simpledialog.askinteger("Nexora AI","Enter the 1st number")
        mm = simpledialog.askinteger("Nexora AI","Enter the 2nd number")
        product= mmm*mm
        messagebox.showinfo("Nexora AI",f"The product of {mmm} and {mm} is {product}")
    else:
        messagebox.showerror("Nexora AI","Invalid Operation")


#Battery Status Checker

def battery_status():
    battery = ps.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged

    if plugged:
        status = "charging"
    else:
        status = "not charging"

    if percent < 20 and not plugged:
        speak(f"{name}, battery sirf {percent}% hai. Please charge.")
    elif percent<=15 and not plugged:
        speak(f"{name} battery is {percent}%. Please wind up your work and I am shutting down the system in 30 seconds.")
        time.sleep(30)
        shutdown()
    return speak(f"Battery is at {percent}% and it is currently {status}.") 

#Intro player

def play_intro_tune():
    pygame.mixer.init()  
    pygame.mixer.music.load(r"FILE_PATH")  
    pygame.mixer.music.play()  

    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)  


#Voice-based AI 

def voice_chatbot():
    speak("Voice chatbot mode activated. Say 'exit' to stop.")
    API_KEY = "API_KEY_HERE"
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat()

    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for your question...")
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
                user_input = r.recognize_google(audio)
                print("You:", user_input)
                if user_input.lower() == "exit":
                    speak("Exiting voice chatbot mode.")
                    break
                response = chat.send_message(user_input)
                print("Nexora:", response.text)

                summarizer = genai.GenerativeModel("gemini-1.5-flash")
                summary = summarizer.generate_content(f"Summarize this in 2-3 lines like you're speaking: {response.text}")
                print("Summary:",summary.text)
                speak(summary.text)

        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, I didn't catch that. Please try again.")

#Password

USER_INPUT=r"FOLDER_PATH"
def login_data():
    if os.path.exists(USER_INPUT):
        with open(USER_INPUT,"r") as f:
            return json.load(f)
    else:
        return {}
def save_users(users):
    with open(USER_INPUT,"w") as f:
        json.dump(users, f)
def password():
    global name
    users=login_data()
    login=simpledialog.askstring("Nexora AI","Enter your password if you are new user type new")
    if login=='new':
        new=simpledialog.askstring("Nexora AI","Enter new password")
        name =simpledialog.askstring("Nexora AI","Enter your name")
        users[new]=name
        save_users(users)
        speak(f"Welcome {name}, Your password has been saved")
        return speak(f"Jai Shree Ram {name}")

    elif login in users:
        name = users[login]
        speak(f"Welcome back {name}")
 
    else:
        messagebox.showerror("Nexora AI","Sorry password not recognized please try again")
        return password()

#Soul of the code


def processCommand(c): 

    for question, answer in cmd.commands.items():
        if question.lower() in c.lower():
            speak(answer)
            return
        
    #Website opener

    if "youtube" in c.lower():
        wb.open("https://youtube.com")
        speak(" Opening YouTube.....")


    elif "instagram" in c.lower():   
        wb.open("https://instagram.com")
        speak("Opening Instagram....")
        

    #App opener

    elif "notepad" in c.lower():
        sb.Popen("notepad.exe")
        speak("Opening Notepad...")
    

    elif "chrome" in c.lower():
        sb.Popen(
            ['start', '', r"ENTER_CHROME_PATH_HERE"],
            shell=True
        )
        speak("Opening Google Chrome...")

    elif "file explorer" in c.lower():
        sb.Popen("explorer.exe")
        speak("Opening File Explorer...")

  #YOU CAN ADD MORE APPS LIKE THIS
   
    # Additional Commands


    elif "shutdown" in c.lower():
        root = tk.Tk()
        root.withdraw()
        response = messagebox.askquestion("Nexora Ai", "Do you want to Shutdown?")
        if response == 'yes':
            speak("Shutting down.....")
            shutdown()
        else:
            speak("No problem I am staying awake....")

    elif "chatbot" in c.lower():

        API_KEY = "API_KEY_HERE"
        genai.configure(api_key=API_KEY)

        model=genai.GenerativeModel("gemini-1.5-flash")

        chat = model.start_chat()

        messagebox.showinfo("Nexora AI","Welcome to Nexora Chatbot mode to quit type exit")
        while True:
            user_input=simpledialog.askstring("Nexora AI","Enter your question")
            if user_input.lower()=='exit':
                break
            response = chat.send_message(user_input)
            messagebox.showinfo("Nexora AI",response.text)
    
    elif "speak" in c.lower():
        voice_chatbot()

    elif "date" in c.lower():
        check_date()

    elif "calculator" in c.lower():
        mathematics()

            
    elif "what's the time" in c.lower():
        user= get_time()
        speak(user)


    elif "battery" in c.lower():
        battery_status()

    elif "question" in c.lower():
      ask_question()

    elif "how long" in c.lower() and ("been running" in c.lower() or "uptime" in c.lower()):
        uptime = get_uptime()
        speak(uptime)

    # Music Player or YouTube Search handler

    elif c.lower().startswith("play"):
       
        query = c.lower().replace("play", "").strip()

        
        if query in music_lib.music:
            link = music_lib.music[query]
            print(f"Song link found: {link}")
            wb.open(link)
            speak(f"Playing {query}")
        else:
            
            search_query = query.replace(" ", "+")  
            url = f"https://www.youtube.com/results?search_query={search_query}"
            wb.open(url)
            speak(f"{name}, playing {query} on YouTube")


    
#Command Listener

def listen_for_commands():
    r = sr.Recognizer()
    while True:
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if "nexora" in word.lower():
                speak(f"{name} I am listening")
                speak("Nexora Active....")
                print("Nexora Active......")

                # Enter command mode
                while True:
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        try:
                            audio = r.listen(source, timeout=5, phrase_time_limit=10)
                            command = r.recognize_google(audio)
                            print(f"Command: {command}")
                            if command.lower() in ["stop listening", "goodbye"] :
                                speak("Exiting command mode. Say 'Nexora' when you need me again.")
                                break
                            processCommand(command)
                        except Exception as e:
                            print(f"Error recognizing command: {e}")
      
        except Exception as e:
            print(f"Error: {e}")



#Code Runner

if __name__ == "__main__":
    pyt.click(1248, 15)
    play_intro_tune()
    messagebox.showinfo("Nexora AI V3","Welcome to Nexora AI Beta Version ")
    password()
    check_date()
    listen_for_commands()
