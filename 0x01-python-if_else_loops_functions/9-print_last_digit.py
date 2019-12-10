#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        temp = (number * -1)
        lastDigit = (int)(temp % 10)
    else:
        temp = number
        lastDigit = (int)(temp % 10)
    print("{:d}".format(lastDigit), end='')
    return lastDigit
