
from ISStreamer.Streamer import Streamer
import time
import requests

streamer = Streamer(bucket_name="Python", bucket_key="python testdata", access_key="zBI3K71GjLbfc1U7o5JZnjCOy5X6Cwe9")


while True:
# data logging

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
	
	streamer.log("My Messages", "Stream Starting")
	for num in range(1, 20):
		time.sleep(0.1)
		streamer.log("My Numbers", num)
		if num%2 == 0:
			streamer.log("My Booleans", False)
		else: 
			streamer.log("My Booleans", True)
		if num%3 == 0:
			streamer.log("My Events", "pop")
		if num%10 == 0:
			streamer.log("My Messages", "Stream Half Done")
	streamer.log("My Messages", "Stream Done")


	#close the stream to properly dispose
	streamer.close()
