## Exercise 01

### Question 01

I think the program will take very slightly longer than the number of times to loop multiplied by the sleep time due to unseen hardware delays.

### Question 02

Before a set or paretheses, such as "int(input())", the "int" and "float" determine the datatype for the value in the parentheses, usually to be assigned to a variable. Changing these will affect how the program will run, possibly turning a value into an integer when a float is needed. After a colon next to a variable name, such as "N: int", "int" and "float" are simply annotations and do not affect the program.

### Question 03

"time.ticks_ms()" has a maximum value and wraps around when it reaches this value. This produces an incorrect when "toc - tic" is used. "time.ticks_diff(toc,tic)" deals with these wrap-around values.

## Exercise 02

### Question 01

Storing the parameters in a JSON file allows us to run the program in the Raspberry Pi on its own without needing input every time we do so. This is especially important on an embedded system because it may be difficult or inconvenient to set up a user interface.

### Question 02

Using a JSON file makes it easier for us to change the parameters if we wish, rather than needing to look through the code to change values.

### Question 03

"os.path.isfile" can't be used because it is not implemented in MicroPython.


