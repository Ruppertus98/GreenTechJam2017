#!/usr/bin/env python2

import speech_recognition as sr
from gtts import gTTS
import os
import requests
import json
import time
import re
import datetime

def speaker(string_to_repeat):
     string_to_repeat = string_to_repeat + "."
     tts = gTTS(text=(string_to_repeat),lang="en")
     tts.save("output_tts.mp3")
     os.system("play output_tts.mp3 2> /dev/null")
  

def listener():
     r = sr.Recognizer()
     with sr.Microphone(sample_rate=44100) as source:
        r.energy_threshold = 3500
        print(r.energy_threshold) 
        print("Say something!")
        audio = r.listen(source)
        with open("microphone-results.wav", "wb") as f:
             f.write(audio.get_wav_data())
  
        try:
              r.recognize_google(audio)
              os.system("play announcement.mp3 2> /dev/null")
              time.sleep(4)
              audio = r.listen(source)
              print("processing")
              what_i_said = r.recognize_google(audio)
              print(what_i_said)
              if ("CO2" in what_i_said):
				r_co2 = requests.get('http://localhost/CO2')
				dic_co2 = r_co2.json() 
				time_co2 = dic_co2.get('time')
				time_output = datetime.datetime.strptime(time_co2, '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%H:%M")
				value_co2 =  dic_co2.get('value')
				speaker("The C02 level at " + time_output + " was " + str(value_co2))
				os.system("rm output_tts.mp3 microphone-results.wav")
        except sr.UnknownValueError:
              print("Google Speech Recognition could not understand your audio")
        except sr.RequestError as e:
              print("Could not request results from Google Speech Recognition service; {0}".format(e))

while True:
	listener()


