# TASK 1_ Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'.
# The type of operator and data are set on the command line when the script is run.
# The script should be launched like this:$ python my_task.py1 * 2
# Notes:For other operations need to raise NotImplementedError.
# Use the argparsemodule to parse command line arguments.
# Your implementation shouldn't require entering any parameters (like -f or --function).

a = float(input("Please, enter a:"))
b = float(input("Please, enter b:"))
print('sum a+b:', a+b)
print('subtraction a-b:', a-b)
print('multiplication a*b:', a*b)
print('division a/b:', a/b)

# TASK 2_ Write a Python-script that performs the standard math functions on the data.
# The name of function and data are set on the command line when the script is run.
# The script should be launched like this:$ python my_task.py add 1 2
# Notes:Function names must match the standard math functions from the built-in libraries.
# The script must raises all happened exceptions.For non-mathematical function need to raise NotImplementedError

import math
x = float(input("Please, enter number:"))
y = input('Please, enter the name of function (sqrt, ceil or floor):')
if y == 'sqrt':
    print('sqrt of x is:', math.sqrt(x))
elif y == 'ceil':
    print('ceil of x is:', math.ceil(x))
elif y == 'floor':
    print('floor of x is:', math.floor(x))
else:
    print('This function was not developed :) have a nice day!')




