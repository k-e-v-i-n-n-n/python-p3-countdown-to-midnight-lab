# your code goes here!
import time


def countdown(num):
    # count = num
    while num > 0:
        format = f'{num} SECOND(S)!'
        print(format)
        num -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(num):
    while num > 0:
        format = f'{num} SECOND(S)!'
        print(format)
        num -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
