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
    pin = `<pin number>` (required)  
    sensorType = `<DHTXX.DHT11 or DHTXX.DHT22>` (optional, default=DHT22)  
    scale = `<DHTXX.FAHRENHEIT or DHTXX.CELCIUS>` (optional, default=FAHRENHEIT)  

2. Call `read()` method, which will return `DHTXXResult` object with actual values and error code.
3. Interpret the DHTXXResult.  The DHTXXResult has a few properties:  
    is_valid(): Returns True or False to indicate if the request was successful.  
    error_code: An integer code representing the error.  
    error_msg: A description of the error.  
    temperature: The returned temperature, or None if an error occurred.  
    humidity: The returned humidity, or None if an error occurred.

These little sensors require some very strict timings to get a good reading. Raspberry Pi's have a hard time being that precise, so invalid readings are frequent - maybe as much as half of all readings fail. That's why it's important to retry until you get a successful reading.

Instead of the read() method, you can also call read_and_retry(attempts), which will automatically retry until it gets a good reading. It will make 10 retries unless you override the number of attempts in the parameter.

Here's an example using the regular `read()` method:

```python
import RPi.GPIO as GPIO
from dhtxx import DHTXX
from time import sleep

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# read data using GPIO #16 pin for a DHT22 sensor with results in FAHRENHEIT
instance = DHTXX(pin=16, sensorType=DHTXX.DHT22, scale=DHTXX.FAHRENHEIT)

while True:
    result = instance.read()
    if result.is_valid():
        print("Temperature: %-3.1f F" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
        break
    else:
        print("Error: %d" % result.error_code)
        sleep(2)
```

ANd here's one using the `read_and_retry()` method:

```python
import RPi.GPIO as GPIO
from dhtxx import DHTXX

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# read data using GPIO #16 pin for a DHT22 sensor with results in FAHRENHEIT
instance = DHTXX(pin=16, sensorType=DHTXX.DHT22, scale=DHTXX.FAHRENHEIT)

result = instance.read_and_retry()
if result.is_valid():
    print("Temperature: %-3.1f F" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)
```

For working examples, see `example.py` and `example2.py` (you may need to adjust pin for your configuration)

# License

This project is licensed under the terms of the MIT license.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
