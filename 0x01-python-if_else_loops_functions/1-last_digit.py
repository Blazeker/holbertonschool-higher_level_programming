#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num2 = number

if number < 0:
    number = -(number)

lastdigit = number % 10
if num2 < 0:
    number = num2
    lastdigit = -(lastdigit)

if lastdigit > 5:
    string = "and is greater than 5"
    print("Last digit of {:d} is {:d}" .format(number, lastdigit), string)
elif lastdigit == 0:
    print("Last digit of {:d} is {:d} and is 0" .format(number, lastdigit))
elif lastdigit < 6:
    string = "and is less than 6 and not 0"
    print("Last digit of {:d} is {:d}".format(number, lastdigit), string)
