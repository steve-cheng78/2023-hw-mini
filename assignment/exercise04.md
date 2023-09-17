# Exercise 04: applications of analog input

[Exercise Python script](./exercise04.py)

[Exercise 04 Questions](#questions)

Taking what we learned in the prior exercises, let's prepare the exercise04.py script for a quality program.
Connect the photocell using the 10k ohm resistor as a voltage divider
[circuit](../doc/circuit.md).

## Questions

Let's "calibrate" the light sensor to be meaningful.
These values will change with room illumination and the specific photocell you have.
We are just getting rough estimates, something other than the default values I used.
Experiment to find approximate max_bright and min_bright values that:

* max_bright: make the LED duty cycle about 100% when in bright light (sunlight, room light)
* min_bright: make the LED duty cycle about 0% when in very dim light (dark room, covered with hand)

Please put these values in the exercise04.json file and read them with your own version of exercise04.py.
This exercise04.json and exercise04.py should be in your own Git repo, and are the "answers" for Exercise 04.

## Notes

Pico MicroPython time.sleep() doesn't error for negative values even though such are obviously incorrect--it is undefined for a system to sleep for negative time.
Experimentally in the "flipped classroom" we found that in this while loop if duty cycle gets larger than 1, the sampling rate slows down!
In any case, duty cycle greater than 1 is undefined.
To be sensible we clip the duty cycle to the range [0, 1].
