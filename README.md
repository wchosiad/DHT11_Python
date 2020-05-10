# DHTXX Python library

This simple class can be used for reading temperature and humidity values from DHT11 and DHT22 sensors on Raspberry Pi.
Thanks to szazo (https://github.com/szazo) for doing most of the heavy lifting

# Installation

To install, clone the repository, cd into it, and run:

```
python3 -m pip install .
```

# Usage

1. Instantiate the `DHTXX` class with the following constructor parameters.
    pin = <pin number> (required)
    sensorType = <DHTXX.DHT11 or DHTXX.DHT22> (optional, default=DHT22)
    scale = <DHTXX.FAHRENHEIT or DHTXX.CELCIUS> (optional, default=FAHRENHEIT)
2. Call `read()` method, which will return `DHT11Result` object with actual values and error code.

Not that these little sensors don't always read successfully every time, you may need to try reading a few times before you get a good value.

For example:

```python
import RPi.GPIO as GPIO
from dhtxx import DHTXX

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# read data using GPIO #16 for DHT22 with results in FAHRENHEIT
instance = DHTXX(pin=16, sensorType=DHTXX.DHT22, scale=DHTXX.FAHRENHEIT)
result = instance.read()

if result.is_valid():
    print("Temperature: %-3.1f F" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)
```

For working example, see `example.py` (you probably need to adjust pin for your configuration)


# License

This project is licensed under the terms of the MIT license.
