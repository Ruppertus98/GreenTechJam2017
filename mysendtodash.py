#!/usr/bin/python

from ISStreamer.Streamer import Streamer
import time
import requests

streamer = Streamer(bucket_name="GreenTechJam", bucket_key="TACC7PKH5CAU", access_key="ziJyzWVUqBFTbsJ2ctybYrxgMqMQrgcf")


while True:
# data logging

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

	dic_window = r_window.json() 
	bool_window =  dic_window.get('open')
	if (bool_window == False):
		window_output = "closed"
		print(window_output)
	else:
		window_output = "opened"
		print(window_output)
		
	
	#dic_heating = r_heating.json() 
	#bool_heating =  dic_heating.get('on')


	streamer.log("Temperature", value_tem)
	streamer.log("Humidity", value_hum)
	streamer.log("CO2", value_co2)
	streamer.log("Window", window_output)
	#streamer.log("Heating", bool_heating)


		#close the stream to properly dispose
	streamer.close()
