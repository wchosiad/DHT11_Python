import RPi.GPIO as GPIO
from dhtxx import DHTXX
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 16. Change the pin to whichever pin you want.
# Also change the sensorType if you are using a DHT11
instance = DHTXX(pin=16, sensorType=DHTXX.DHT22, scale=DHTXX.FAHRENHEIT)

try:
    result = instance.read_and_retry()
    if result.is_valid():
        print("       Time: " + str(datetime.datetime.now()))
        print("Temperature: %-3.1f F" % result.temperature)
        print("   Humidity: %-3.1f %%" % result.humidity)
    else:
        print(result.error_msg)

    print("----------------------------------")
except:
    raise()

GPIO.cleanup()
