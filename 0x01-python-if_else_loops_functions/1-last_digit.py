#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    temp = (number * -1)
    lastDigit = -1 * (int)(temp % 10)
else:
    temp = number
    lastDigit = (int)(temp % 10)
if (lastDigit > 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(
        number, lastDigit))
elif (lastDigit < 6 and lastDigit != 0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(
        number, lastDigit))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastDigit))
