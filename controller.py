#!/usr/bin/python

import requests
import json
import time


while True:
	r_co2 = requests.get('http://localhost:8000/CO2')
	r_hum = requests.get('http://localhost:8000/humidity')
	r_tem = requests.get('http://localhost:8000/temperature')
	r_window = requests.get('http://localhost:8000/window')
	r_heating = requests.get('http://localhost:8000/heating')
	
	dic_co2 = r_co2.json() 
	time_co2 = dic_co2.get('time') 
	value_co2 =  dic_co2.get('value')

	dic_hum = r_hum.json() 
	time_hum = dic_hum.get('time') 
	value_hum =  dic_hum.get('value')

	dic_tem = r_tem.json() 
	time_tem = dic_tem.get('time') 
	value_tem =  dic_tem.get('value')

	window_set = r_window.json().get('open')
	heating_set = r_heating.json().get('on') 
	
	if (value_co2 > 800 and value_tem > 30 and value_hum > 70):
		window_set = True
		heating_set = False
		print("case 1")
	elif (value_co2 < 500 and value_tem < 18 and value_hum < 50):
		window_set = False
		print("case 2")
	
	elif (value_tem < 10):
		window_set = False
		heating_set = True
		print("case 3")


	requests.post('http://localhost:8000/window',  data = {'open':window_set})
	requests.post('http://localhost:8000/heating',  data = {'on':heating_set})
	
	time.sleep(5)
