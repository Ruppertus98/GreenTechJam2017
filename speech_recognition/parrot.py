#!/usr/bin/env python2

import speech_recognition as sr
from gtts import gTTS
import os
  
def repeater(string_to_repeat):
     string_to_repeat = string_to_repeat + "."
     tts = gTTS(text=(string_to_repeat),lang="en")
     tts.save("output_tts.mp3")
     os.system("play output_tts.mp3")
  
def listener():
     r = sr.Recognizer()
     with sr.Microphone(sample_rate=44100) as source:
         print("Say something!")
         audio = r.listen(source)
         with open("microphone-results.wav", "wb") as f:
             f.write(audio.get_wav_data())
  
         try:
              print("processing")
              what_i_said = r.recognize_google(audio)
              print("Google Speech Recognition " + what_i_said)
              repeater(what_i_said)
              os.system("rm output_tts.mp3 microphone-results.wav")
         except sr.UnknownValueError:
              print("Google Speech Recognition could not understand your audio")
         except sr.RequestError as e:
              print("Could not request results from Google Speech Recognition service; {0}".format(e))

while True:
	listener()
