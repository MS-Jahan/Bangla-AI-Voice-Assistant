import speech_recognition as sr
from banglaspeech2text import Speech2Text
# from googletrans import Translator
import requests, time
from Bard import Chatbot
from gtts import gTTS
from playsound import playsound
from banglatts import BanglaTTS
import json
import os

from config import *
from selenium_helpers import get_cookies

tts = BanglaTTS(save_location="save_model_location")

print("Staring the AI...")

Secure_1PSID, Secure_1PSIDTS = '', ''

with open('cookies.json', 'r') as fp:
        cookies = json.load(fp)
        for cookie in cookies:
            if cookie['name'] == '__Secure-1PSID':
                Secure_1PSID = cookie['value']
            elif cookie['name'] == '__Secure-1PSIDTS':
                Secure_1PSIDTS = cookie['value']

# print("Secure_1PSID:", Secure_1PSID)
# print("Secure_1PSIDTS:", Secure_1PSIDTS)

try:
    ai = Chatbot(Secure_1PSID, Secure_1PSIDTS)
except Exception as e:
    print("Error: ", e)
    print("Trying to get cookies...")
    Secure_1PSID, Secure_1PSIDTS = get_cookies()
    # print("Secure_1PSID:", Secure_1PSID)
    # print("Secure_1PSIDTS:", Secure_1PSIDTS)
    ai = Chatbot(Secure_1PSID, Secure_1PSIDTS)

stt = Speech2Text(model="base")

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, phrase_time_limit = 16)
    print("Recognizing...")
    output = None
    try:
        print("Using Google API...")
        output = r.recognize_google(audio, language = 'bn')
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except Exception as e:
        print("Error: ", e)
    
    if output is None:
        print("Using OpenAI Whisper Model...")
        output = stt.recognize(audio)

    print("From voice:", output)
    
    api_response = ai.ask(prompt + output + "\n ৫০ শব্দে এর উত্তর দাও।")['content']
    print("api:", api_response)
    try:
        gtts = gTTS(api_response, lang='bn')
        gtts.save('hello.mp3')
        # playsound('hello.mp3')
        os.system(".\mpv\mpv.com --audio-display=no --no-video --no-terminal hello.mp3")
    except Exception as e:
        print("Error: ", e)
        path = tts(api_response, voice='female', filename='1.wav')
        # playsound('1.wav')
        os.system(".\mpv\mpv.com --audio-display=no --no-video --no-terminal 1.wav")






'''
Using Google API...
From voice: আমার নাম কি তোমাকে কে তৈরি করেছে সংক্ষেপে বলো
api: আমার নাম অনন্যা। আমাকে তৈরি করেছে আইএসটি (ইনস্টিটিউট অফ সাইন্স এন্ড টেকনোলজি, বাংলাদেশ) এর কিছু শিক্ষার্থী। তারা আমাকে একটি বড় ভাষা মডেল হিসেবে তৈরি করেছে যা পাঠ্য তৈরি করতে, ভাষা অনুবাদ করতে, বিভিন্ন ধরনের সৃজনশীল সামগ্রী লিখতে এবং তথ্যপূর্ণ উপায়ে প্রশ্নের উত্তর দিতে সক্ষম।
'''