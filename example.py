import RPi.GPIO as GPIO
from dhtxx import DHTXX
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 16. Change the pin to whichever pin you want.
instance = DHTXX(pin=16, sensorType=DHTXX.DHT22, scale=DHTXX.FAHRENHEIT)

try:
	runs = 0
	errors = 0
	while True:
		runs = runs + 1
		try:
			result = instance.read()
			if result.is_valid():
				print("       Time: " + str(datetime.datetime.now()))
				print("Temperature: %-3.1f F" % result.temperature)
				print("   Humidity: %-3.1f %%" % result.humidity)
				print("----------------------------------")
			else:
				errors = errors + 1
				rate = float(errors/runs) * 100.0
				print("Invalid result. Error rate: %-3.1f %%" % rate)
				print("----------------------------------")
		except:
			raise()

		time.sleep(3)
except KeyboardInterrupt:
	print("Cleanup")
	GPIO.cleanup()