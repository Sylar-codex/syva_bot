import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from  time import ctime

from facial_recognition_check.face_match import check_face_match

r = sr.Recognizer()

if not check_face_match() :
    # time.sleep(1)
    # syva_speak('I do not recognize you')
    pass

else :
    print(check_face_match())
    
    def syva_speak(audio_string) :
        tts = gTTS(text=audio_string, lang='en')
        r = random.randint(1, 10000000)
        audio_file = 'audio-' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(audio_string)
        os.remove(audio_file)

    time.sleep(1)
    syva_speak('Welcome my Lord, Victor, how may I help you?')

    def record_audio(ask= False) :
        with sr.Microphone() as source :
            if ask:
                syva_speak(ask)
            audio = r.listen(source)
            voice_data= ''
            try:
                voice_data = r.recognize_google(audio)
                print(voice_data)
            except sr.UnknownValueError :
                syva_speak('sorry, I did not get that')
            except sr.RequestError :
                syva_speak('sorry, my speech service is down')

            return voice_data


    def respond(voice_data) :
        if 'who is your creator' in voice_data :
            syva_speak('You my Lord, Victor')
        if 'what is your name' in voice_data :
            syva_speak('my name is Syva')
        if 'what time is it' in voice_data :
            syva_speak(ctime)
        if 'search' in voice_data :
            search = record_audio('what do you want to search for?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            syva_speak('Here is what i found for' + search)
        if 'find location' in voice_data :
            location = record_audio('what is the location?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            syva_speak('Here is the location of ' +location)
        if 'exit' in voice_data :
            exit()

    while 1:
        voice_data = record_audio()
        respond(voice_data) 




