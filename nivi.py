import os
import pygame
import speech_recognition as sr
from test import *
from time import sleep

def speak(text):
    
    # python_path = r'C:\users\nithin\anaconda3\python.exe'  # Replace with your actual Python path
    voice = "en-US-AriaNeural"
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'
    
    os.system(command)
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            clock = pygame.time.Clock()
            clock.tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    
    
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
    
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=5)
        print(" Iam Listening...")
        audio =r.listen(source, timeout=5)

        print("you can speak now..")
        r.pause_threshold=0.8
        audio=r.listen(source, timeout=5)
    
    try:
        print("recognizing..")
        query=r.recognize_google(audio,language='en-us')
    except Exception as e:
        print(e)
        return ""
    return query

speak("hello, I am your virtual assistant nivi. How can I help you today!")

chatnumber=2
while True:
    
    def retriveData():
        sendQuery(take_command())
        sleep(15)
        print('Retriving Chat...')
        sleep(1)
        global p
        global chatnumber
        p = driver.find_element(By.XPATH, f'/html/body/div/div/div/div[2]/div[1]/div/div/div[{chatnumber}]/div/div[2]/div/div/div/div/div/p')
        chatnumber+=2
        print("\nNIVI: " + p.text)
        
        nivi=p.text
        return(p.text)
    retriveData()
    speak(p.text)

    sleep(5)

