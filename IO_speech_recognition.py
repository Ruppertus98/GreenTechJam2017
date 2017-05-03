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
  
def CO2out():
	r_co2 = requests.get('http://localhost:8000/CO2')
	dic_co2 = r_co2.json() 
	time_co2 = dic_co2.get('time')
	time_output = datetime.datetime.strptime(time_co2, '%Y-%m-%dT%H:%M:%S.%f').strftime("%H:%M")
	value_co2 =  dic_co2.get('value')
	speaker("The C02 level at " + time_output + " was " + str(value_co2))
	if (value_co2 > 800):
		check = requests.get('http://localhost:8000/window')
		bool_window = check.json().get('open')
		if(bool_window == False):
			speaker("I'm going to open your window")
		else:
			speaker("Your window is already opened, starting ventilation")
	elif (value_co2 < 600):
		speaker("I'm going to close your window")
	
def window_control(what_i_said):
	win_stat = requests.get('http://localhost:8000/window')
	bool_window = win_stat.json().get('open')
	if (bool_window == False):
			window_output = "closed"
	else:
			window_output = "opened"
	if("status" in what_i_said):
		speaker("Your window is " + window_output)
	elif("open" in what_i_said):
		if (bool_window == False):
			speaker("Opening the windows")
			requests.post('http://localhost:8000/window',  data = {'open':True})
		else:
			speaker("Your window is already opened")
	elif("close" in what_i_said):
		if (bool_window == True):
			speaker("Closing the windows")
			requests.post('http://localhost:8000/window',  data = {'open':False})
		else:
			speaker("Your window is already closed")
	else:
		speaker("Your window is " + window_output)
	
	
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
                CO2out()
                os.system("rm output_tts.mp3 microphone-results.wav")
              elif("window" in what_i_said):
                window_control(what_i_said)
        except sr.UnknownValueError:
              speaker("I did not understand that")
              time.sleep(2)
        except sr.RequestError as e:
              speaker("Could not request results from Google Speech Recognition service; {0}".format(e))
              time.sleep(2)
while True:
	listener()


