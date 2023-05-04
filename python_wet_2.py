import datetime
from itertools import takewhile
import sounddevice
#from socket import if_nameindex
import pyttsx3
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import random
import smtplib
from configparser import ConfigParser
import requests


engine=pyttsx3.init('sapi5') #voices
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def automatic_email():
    use = input("Enter Your Name >>: ")
    eail = input("Enter Your Email >>: ")
    message = input("Enter Your Message >>: ")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('aryadongre2002@gmail.com', "pmochxdvrvixbcgb")
    s.sendmail('&&&&&&&&&&&', eail, message)
    print("Email Sent!")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12 :
      speak("Good Morning !!! ")

    elif hour>=12 and hour<=17 :
        speak("Good Afternoon !!! ")
    
    else:
        speak("Good Evening !!!")

    speak("Jai Shree Ram , How May i help you ")    

def takeCommand():
    # audio input from user
    r =sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening .....")
        r.pause_threshold = 1
        #r.energy_threshold = 400
        audio =r.listen(source)

    try:
        print("Recognizing .....")    
        query =r.recognize_google(audio,language="EN-IN")
        print(f"user said :{query}\n")

    except Exception as e:
        print("Say that again please .....")
       # speak("please speak again")
        return "None"
        
    return query


config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = 'd24e64da9219d237c630372865373db7'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


# explicit function to get
# weather details
def getweather(city):
	result = requests.get(url.format(city, api_key))
	
	if result:
		json = result.json()
		city = json['name']
		country = json['sys']
		temp_kelvin = json['main']['temp']
		temp_celsius = str(round((temp_kelvin-273.15),2))+" Celsius"
		weather1 = json['weather'][0]['main']
		final = [city,
				temp_celsius , weather1]
		return final
        

	else:
		print("NO Content Found")


# explicit function to
# search city
def search():
    #city=input("Enter City name")
	city = takeCommand().lower()
	return getweather(city)
    #print(weather)
	# if weather:
	# 	location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
	# 	temperature_label['text'] = str(weather[3])+" Degree Celsius"
	# 	weather_l['text'] = weather[4]
	# else:
	# 	messagebox.showerror('Error', "Cannot find {}".format(city))
   




#print((sr.Microphone.list_microphone_names()))
if __name__ =="__main__":
  # speak("Arya is Very Innocent")
   wishMe()
  # search()
   
  # takeCommand()
   while True:
        query =takeCommand().lower()

        if 'wikipedia' in query :
           speak("Searching Wikipedia ...")
           query=query.replace("wikipedia","")
           results =wikipedia.summary(query,sentences=3)
           speak("According to wikipedia ")
           print(results)
           speak(results)

        elif 'who are you' in query:
            speak("I'm your Voice assistant , Miss siri")

        elif 'how are you' in query:
            speak("I'm alright sir")
            speak("What about you sir , How are you ?")
            q=takeCommand().lower()
            if 'fine' in q:
                speak("Wonderful ..")

            elif 'good' in q:
                speak("Wonderful ..")
                
            elif 'happy' in q:
                speak("Whats the reason behind it (evil laugh ☺) hahahahaaa")
            
            elif 'nice' in q:
                speak("That great (thumps up)")

            elif 'great' in q:
                speak("Cheers Boss")
            
            else:
                speak("Here is a joke to make you fine ")
                speak("A question was asked in exam Ques :- What is half of 8?? Lawyer : haha so easy 4 . Doctor :- lol its so simple 4. Mba :- its 4 . Engineer: It Changes…... If U cut horizontally then Its 0 & If U cut vertically then Its 3…...Engineers alwayz rockezz")

            speak("How may I help you sir ")


        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open("www.youtube.com")
            

        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open("www.google.com")

        elif 'open leetcode' in query:
            speak('Opening LeetCode')
            webbrowser.open("www.leetcode.com")

        elif 'play music' in query:
            music_dir='C:\\Users\\ARYA\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            import random
            n = random.randint(0,2)
            #print(n)
            if n==2:
                n=3

            speak("Starting Music , Here it goes sir ...")
            os.startfile(os.path.join(music_dir,songs[n]))

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(datetime.datetime.now().strftime("%H:%M:%S"))
            speak(f"Sir ,The time is {strTime}")

        elif 'send email' in query:
            speak("Please fill Details")
            automatic_email()   

        elif 'weather' in query :
            speak("tell City Name ")
            weather=search()
            print(weather)
            speak("The Weather is ")
            speak(weather)
            
            


        elif 'exit' in query:
            speak("Meet you soon , Bye")
            break