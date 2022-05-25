from pyttsx3 import speak, init
from datetime import datetime
import speech_recognition as sr
import wikipedia
from youtubesearchpython import *
import webbrowser
import os
import sys
from time import *
from pydbpedia import PyDBpedia, namespace
import pandas as pd


def name(name):
    word=list(name.split())
    t_name=""
    for i in word:
        t_name+=i+"_"
    query="http://dbpedia.org/resource/"+t_name[:-1]
    query2="http://dbpedia.org/page/"+t_name[:-1]
    dbpedia_uris = [query]

    dbpedia_wrapper = PyDBpedia(endpoint="http://dbpedia.org/sparql")
    objects=dbpedia_wrapper.get_objects(subjects=dbpedia_uris, predicates=[namespace.RDF_TYPE])
    data=pd.DataFrame(objects)
    print(data.head(10))

engine = init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def kaam():
    print("It may be possible that some of my fuctionality may not work becouse I am in development phase, you may find bugs also. Apologies for the inconvenience caused.")
    speak("It may be possible that some of my fuctionality may not work becouse I am in development phase, you may find bugs also. Apologies for the inconvenience caused.")
    speak("Here is what i can do for you. Try to ask these commands")
    print("Here is what i can do for you. \n 1. Search on web \n 2. Exact date and time update \n 3. Your exact location \n 4. Open some of the aplications (like YouTube and many more) \n 5. Make/Delete Folders on diffrent locations of your system \n 6. Make/Delete File on diffrent locations of your system \n 7. Shut Down/Restart Your System \n 8. Exit Omniscient \n And many more things that you expect")
    speak("Search on web  \n Exact date and time update  \n Your exact location  \n Open some of the aplications (like YouTube and many more) \n Make Delete Folders on diffrent locations of your system \n Make Delete File on diffrent locations of your system  \n Shut Down Restart Your System  \n Exit Omniscient And many more things that you expect")

def wishme(maalik):
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        print(f"Good Morning {owner_name}!\n")
        speak(f"Good Morning {owner_name}!")
    elif hour >= 12 and hour < 18:
        print(f"Good Afternoon {owner_name}!\n")
        speak(f"Good Afternoon {owner_name}!")
    elif hour >= 18 and hour < 24:
        print(f"Good Evening {owner_name}!\n")
        speak(f"Good Evening {owner_name}!")
    speak(f"{owner_name} what to do.")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pass_thrushold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query} \n")
    except Exception as e :
        speak(" please check you command  and say that again please...")
        return "none"
    return query


def tk(var):
     speak(var)
     r = sr.Recognizer()
     with sr.Microphone() as source:
         r.pass_thrushold = 0.2
         audio = r.listen(source)
     query = r.recognize_google(audio)
     return query

if __name__ == '__main__':
     speak("Please tell me your name.")
     print("Please tell me your name.")
     owner_name=takecommand()
     while owner_name =='none':
         owner_name=takecommand()
     wishme(owner_name)
while True:
        query = takecommand().lower()
        if 'who are you' in query:
            speak('My name is Omniscient but you can call me ohm')
            print('My name is Omniscient but you can call me ॐ')
        elif 'what is the time' in query:
            print(ctime())
            speak(f"{owner_name} the time is :" + ctime())

        elif "search person" in query:
            speak("who do you want to search ")
            a=takecommand()
            name(a)
            try:
                result = wikipedia.summary(a, sentences=2)
                url = 'https://google.com/search?q=' + a
                webbrowser.get().open(url)
            except:
                url = 'https://google.com/search?q=' + a
                webbrowser.get().open(url)
            speak("According to wikipedia:")
            print(result)
            speak(result)
        elif 'wikipedia' in query or "search" in query:
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                url = 'https://google.com/search?q=' + query
                webbrowser.get().open(url)
            except:
                url = 'https://google.com/search?q=' + query
                webbrowser.get().open(url)
            speak("According to wikipedia:")
            print(result)
            speak(result)
        elif 'my location' in query:
            webbrowser.open("https://www.google.com/maps/place")
            speak("Hold on {owner_name}, I will show you where.")   
        elif 'gaana' in query or 'song'  in query or 'music' in query or "gana" in query:
            speak("which song you want to play.")
            name = takecommand()
            videosSearch = VideosSearch(name, limit = 2)
            a=videosSearch.result()
            webbrowser.open(a['result'][0]['link'])

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif "copy" in query:
            speak("form which drive you want to copy")
            e = takecommand().upper()
            speak("please tell the file name")
            f = takecommand()
            speak("please tell the extention")
            g = takecommand()
            h = e + "://" + f + "." + g
            speak("please tell the drive name where you want to paste the file:")
            a = takecommand()
            speak("please tell the name of your new file if you want to change:")
            b = takecommand()
            speak("please tell the extentin of your file")
            c = takecommand()
            d = a + "://" + b + "." + c
            with open(h, "r") as fil:
                with open(d, "a")as lit:
                    for line in fil:
                        print(line, file=lit)

        elif 'github' in query:
            webbrowser.open("github.com")
        elif 'open youtube' in query or 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'video' in query:
            video_dir = 'D:\\videos'
            video = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, video[0]))
        elif 'kuch nahi'in query or 'nahi' in query:
            speak("Ok {owner_name}")
            time.sleep(5)
        elif 'make folder' in query or 'folder banao' in query:
            speak(f"{owner_name} in which folder you want to make.. please select the destination folder from below..")
            print(" Documents \n Desktop \n downloads")
            query=takecommand().lower()
            if 'documents' in query:
                speak(f"{owner_name} tell the name please..")
                a=takecommand().lower()
                b = "mkdir "
                c = b + a
                command="cd Documents && {}".format(c)
                os.system(command)
                speak("Folder is Created with name ")
                speak(a)
                speak(f"{owner_name} tell Next task please..")
                
            elif 'desktop' in query:
                speak(f"{owner_name} tell the name please..")
                a=takecommand().lower()
                b = "mkdir "
                c = b + a
                command="cd Desktop && {}".format(c)
                os.system(command)
                speak("Folder is Created with name ")
                speak(a)
                speak(f"{owner_name} tell Next task please..") 
                
            elif 'downloads' in query:
                speak(f"{owner_name} tell the name please..")
                a=takecommand().lower()
                b = "mkdir "
                c = b + a
                os.system('cd downloads')
                os.system(c)
                print(c)
                speak("Folder is Created with name ")
                speak(a)
                speak(f"{owner_name} tell Next task please..")
        elif 'delete folder' in query:
            speak(f'{owner_name},From which destination you want to delete the folder.. please choose destination from below.')
            print(' Documents \n Desktop \n Downloads')
            if 'documents' in query:
                a =takecommand(speak(f"{owner_name} tell the name please.."))
                b = "rmdir "
                c = b + a
                os.system('cd documents') 
                os.system(c)
            elif 'downloads' in query:
                a = takecommand(speak(f"{owner_name} tell the name please.."))
                b = "rmdir "
                c = b + a
                os.system('cd downloads')
                os.system(c)
            elif 'desktop' in query:
                a = takecommand(speak(f"{owner_name} tell the name please.."))
                b = "rmdir "
                c = b + a
                os.system('cd desktop')
                os.system(c)
        elif 'make file' in query or 'file banao' in query or 'file' in query:
            
            speak('tell the name of directory in which you want to make file.. please choose the directory that are listed below')
            print(' Documents \n Desktop \n Downloads')
            dirr=takecommand().lower()
                                        
            if dirr == 'desktop':
                
                speak(f"{owner_name} tell the name of file please..")
                a =takecommand()
                
                b = "notepad "
                speak(f"{owner_name} please tell extension of the file :")
                d = takecommand()
                
                e = '.'
                c = b + a + e + d
                os.system('cd desktop')
                os.system(c)
            elif dirr == 'downlaods' or dirr == 'download':
                a = input(speak(f"{owner_name} tell the name of file please.."))
                b = "notepad "
                d = input(speak(f"{owner_name} please tell extension of the file :"))
                e = '.'
                c = b + a + e + d
                os.system('cd downlaods')
                os.system(c)
            elif dirr == 'documents' or dirr == 'document':
                a = input(speak(f"{owner_name} tell the name of file please.."))
                b = "notepad "
                d = input(speak(f"{owner_name} please tell extension of the file :"))
                e = '.'
                c = b + a + e + d
                os.system('cd documents')
                os.system(c)
       
        elif 'shutdown' in query:
            os.system("shutdown /s /t 5")
            speak(f"{owner_name}.. your pc will shutdown with in 10 seconds.")
            exit()
        elif 'restart' in query:
            os.system("shutdown /r /t 5")
            speak(f"{owner_name}, restarting system with in 10 seconds")
        elif "what can you do for me" in query or "what can you do" in query  or "what are you capable of" in query or "capability" in query:
            kaam()
        elif 'exit' in query or 'band ho' in query or 'close' in query:
            speak(f"have a good day, {owner_name}")
            sys.exit()

        
        else:
            speak("sorry i didn't understand please say it again..")
            print("Sorry I didn't understand, please say it again..")