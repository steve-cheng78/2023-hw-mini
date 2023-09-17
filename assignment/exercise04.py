"""
Use analog input with photocell
"""

import time
import machine
import json
import os


def get_params(param_file: str) -> dict:
    """Reads parameters from a JSON file."""
    
    with open(param_file) as f:
        params = json.load(f)

    return params

led = machine.Pin("LED", machine.Pin.OUT)
adc = machine.ADC(28)

blink_period = 0.1

params = get_params("exercise04.json")

print("this is params")
print(params)

max_bright = params["max_bright"]
min_bright = params["min_bright"]

while True:
    value = adc.read_u16()
    #print(value)
    duty_cycle = (value - min_bright) / (max_bright - min_bright)
    
    print(duty_cycle)
    
    led.high()
    time.sleep(blink_period * duty_cycle)
    led.low()
    time.sleep(blink_period * (1 - duty_cycle))
