import pyttsx3  # give voice to what is typed using init( )
import speech_recognition as sr  # convert user audio into written format
import webbrowser  # opens websites using open( )
import datetime  # gives current date and time using now( )
from time import sleep  # gives delay after executing one line using sleep( )
import pywhatkit  # plays recent vedio on youtube using playonyt( )
from os import startfile
from pyautogui import click
from keyboard import press_and_release as pr
from keyboard import press
from keyboard import write
import subprocess as sp
import os


def sptext():

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data

        except sr.UnknownValueError:
            print("Trying my best")


def speechtx(x):

    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)
    engine.say(x)
    engine.runAndWait()


def greet():

    command = sptext().lower()
    if "jarvis" in command:
        speechtx("Initializing. ")
        # time.sleep(3)
        speechtx("All wrapped up sir. How are you")
        return

    else:
        speechtx("Sorry sir . Call me by my name")
        return 0


def youtube_search(command):
    result = ("https://www.youtube.com/results?search_query="+command)
    speechtx("roger that")
    # print(result)
    webbrowser.open(result)
    pywhatkit.playonyt(command)


def google_serch(command):
    result = ("https://www"+"."+command+".com/")
#   print(result)
    speechtx("Roger that")
    webbrowser.open(result)


def whatsapp_msg(name, msg):
    pr('cmd')
    sleep(1)
    click(x=670, y=329)  # watsapp on pinned apps
    sleep(2)
    click(x=152, y=142)  # for search menu
    sleep(2)
    write(name)
    sleep(1)
    click(x=239, y=215)  # for open account
    sleep(1)
    click(x=870, y=979)  # click on chat
    sleep(2)
    write(msg)
    sleep(1)
    press('enter')


def whatsapp_call(name):
    pr('cmd')
    sleep(1)
    click(x=670, y=329)  # watsapp on pinned apps
    sleep(2)
    click(x=152, y=142)  # for search menu
    sleep(1)
    write(name)
    sleep(1)
    click(x=239, y=215)  # for open account
    sleep(1)
    click(x=1777, y=89)


# if __name__ == '__main__':
def Task_Gui():
  
    print("")
    k = greet()
    if (k == 0):
        print("Thank you")
    else:
    
        while (True):
                   
            command = sptext().lower()

            if "who are you" in command:
              speechtx( "I am Jarvis. A global peacekeeping program designed by Mr. Stark. Always ready to help you master . ")

            elif "do" in command:
              speechtx("I can do many stuff for you , like updating time , opening search and much more ")

            elif "fine" in command:
              speechtx("Nice to hear that. what can i do for you")

            elif 'time'  in command:
             time = datetime.datetime.now().strftime("%I%M%p")
             speechtx("Time is ")
             speechtx(time)

            elif 'exit'in command:
              speechtx("As always sir. It was  a great pleasure watching your work.")
              os.startfile("C:\\Users\\hussain\\Desktop\\python assistant\\waake_up.py")
              sleep(2)
              pr('Ctrl+k')
              break

            elif 'open' in command:
              query = command.replace("open ",'')
              google_serch(query)

            elif 'youtube' in command :
              query = command.replace("on youtube","")
              Query = query.replace("search","")
              command =Query.replace("play","")
              youtube_search(command)

            elif 'message' in command :
              speechtx("whom do you want to send")
              name=sptext()

              speechtx("What is the message")
              msg=sptext()

              whatsapp_msg(name,msg)

            elif 'call' in command :
              name = command.replace("call","")
              whatsapp_call(name)
