import RPi.GPIO as GPIO
from dhtxx import DHTXX
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 16
instance = DHTXX(pin=16, sensorType=DHTXX.DHT22, scale=DHTXX.FAHRENHEIT)

try:
	while True:
		try:
			result = instance.read()
			if result.is_valid():
				print("Last valid input: " + str(datetime.datetime.now()))
				print("Temperature: %-3.1f F" % result.temperature)
				print("Humidity: %-3.1f %%" % result.humidity)
				print("----------------------------------")
#			else:
#				print("invald result")
		except:
			raise()

		time.sleep(3)
except KeyboardInterrupt:
	print("Cleanup")
	GPIO.cleanup()