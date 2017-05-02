#!/usr/bin/python

import requests
import json
import time


while True:
	r_co2 = requests.get('http://localhost:8000/CO2')
	r_hum = requests.get('http://localhost:8000/humidity')
	r_tem = requests.get('http://localhost:8000/temperature')
	
	dic_co2 = r_co2.json() 
	time_co2 = dic_co2.get('time') 
	value_co2 =  dic_co2.get('value')

	dic_hum = r_hum.json() 
	time_hum = dic_hum.get('time') 
	value_hum =  dic_hum.get('value')

	dic_tem = r_tem.json() 
	time_tem = dic_tem.get('time') 
	value_tem =  dic_tem.get('value')

	print(value_co2)
	print(value_hum)
	print(value_tem)
	
	if (value_co2 > 800):
		requests.post('http://localhost:8000/window',  data = {'open':'true'})
		requests.post('http://localhost:8000/heating',  data = {'on':'false'})
	elif (value_co2 < 600):
		requests.post('http://localhost:8000/window',  data = {'open':'true'})
	if (value_tem > 30):
		requests.post('http://localhost:8000/window',  data = {'open':'true'})
		requests.post('http://localhost:8000/heating',  data = {'on':'false'})
	elif (value_tem < 20):
		requests.post('http://localhost:8000/window',  data = {'open':'true'})
	elif (value_tem < 10):
		requests.post('http://localhost:8000/heating',  data = {'on':'false'})
	if (value_hum > 70):
		requests.post('http://localhost:8000/window',  data = {'open':'true'})
		requests.post('http://localhost:8000/heating',  data = {'on':'false'})
	if (value_hum < 50):
		requests.post('http://localhost:8000/window',  data = {'open':'true'})
	time.sleep(1)
