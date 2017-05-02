
from ISStreamer.Streamer import Streamer
import time
import requests

streamer = Streamer(bucket_name="Python", bucket_key="python testdata", access_key="zBI3K71GjLbfc1U7o5JZnjCOy5X6Cwe9")


#while True:
# data logging

	#r_co2 = requests.get('http://localhost:8000/CO2')
	#r_hum = requests.get('http://localhost:8000/humidity')
	#r_tem = requests.get('http://localhost:8000/temperature')
	
#dic_co2 = r_co2.json() 
#time_co2 = dic_co2.get('time') 
#value_co2 =  dic_co2.get('value')
value_co2 = 5

#dic_hum = r_hum.json() 
#time_hum = dic_hum.get('time') 
#value_hum =  dic_hum.get('value')
value_hum = 89

#dic_tem = r_tem.json() 
#time_tem = dic_tem.get('time') 
#value_tem =  dic_tem.get('value')
value_tem = 10

streamer.log("Temperature", value_tem)
streamer.log("Humiture", value_hum)
streamer.log("CO2", value_co2)


	#close the stream to properly dispose
streamer.close()
