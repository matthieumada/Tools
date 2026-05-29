import time
import machine

"""
Code to use a tilt sensor to contorl a LED. When the tilt sensor is tilted, the LED will turn on, otherwise it will turn off.
put on either GPIO4 GPIO 19,21"""
# pin setting
led = machine.Pin(13, machine.Pin.OUT)
tilt_sensor = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    print(f"tilt sensor value:{tilt_sensor.value()}")
    
    if tilt_sensor.value() == 1:
        print("LED ON")
        led.value(1)
    else:
        print("LED OFF")
        led.value(0)

