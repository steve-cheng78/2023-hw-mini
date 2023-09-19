"""
use two simultaneously running threads to:

* read Photocell periodically and save to JSON file
* code similar to your project01.py in a second thread simultaneously
"""

import machine
import time
import _thread
import json

import project01

# project01.py also needs to be copied to the Pico

def photocell_logger(N: int, sample_interval_s: float) -> None:
    """
    get raw uint16 values from photocell N times and save to JSON file

    Parameters
    ----------

    N: int
        number of samples to take
    """

    print("start light measurement thread")

    adc = machine.ADC(28)

    values: list[int] = []

    start_time: tuple[int] = time.localtime()

    for _ in range(N):
        values.append(adc.read_u16())
        time.sleep(sample_interval_s)

    end_time: tuple[int] = time.localtime()
    # please also log the end_time and sample interval in the JSON file
    #  i.e. two additional key, value in the dict

    data = {
        "light_uint16": values,
        "start_time": start_time,
    }

    now: tuple[int] = time.localtime()

    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"proj2-light-{now_str}.json"

    print("light measurement done: write", filename)

    project01.write_json(filename, data)

def get_params(param_file: str) -> dict:
    """Reads parameters from a JSON file."""
    
    with open(param_file) as f:
        params = json.load(f)

    return params

def scorerMulti(t: list[int | None]) -> None:
    # %% collate results
    
    for i in t:
        misses = i.count(None)
        print(f"Player {i}: You missed the light {misses} / {len(t)} times")

        t_good = [x for x in i if x is not None]

        max_t = max(t_good)
        min_t = min(t_good)
        avg_t = sum(t_good)/len(t_good)
        score = len(t_good)/N
        
        print(t_good)
        print(max_t)
        print(min_t)
        print(avg_t)

        # add key, value to this dict to store the minimum, maximum, average response time
        # and score (non-misses / total flashes) i.e. the score a floating point number
        # is in range [0..1]
        data[i] = {"response times" : t_good,
                "max_time" : max_t,
                "min_time" : min_t,
                "average_time" : avg_t,
                "score" : score
                }

        # %% make dynamic filename and write JSON

    filename = f"proj2-light.json"

    print("write", filename)

    write_json(filename, data)


def blinker_response_game(N: int) -> None:
    # %% setup input and output pins
    led = machine.Pin("LED", machine.Pin.OUT)
    button1 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
    button2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

    # %% please read these parameters from JSON file like project 01 instead of hard-coding
    params = get_params("project02.json")
    
    on_ms = params["on_ms"]
    
    t1: list[int | None] = []
    t2: list[int | None] = []
    
    project01.blinker(3, led)
    
    for i in range(N):
        time.sleep(project01.random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        ta = None
        tb = None

        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            
            if button1.value() == 0:
                ta = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                
            if button2.value() == 0:
                tb = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                
            if ta is not None and tb is not None:
                break
            
        t1.append(ta)
        t2.append(tb)

        led.low()

    project01.blinker(5, led)

    t = [t1, t2]
    scorerMulti(t)

_thread.start_new_thread(photocell_logger, (10, 0.5))
blinker_response_game(10)
