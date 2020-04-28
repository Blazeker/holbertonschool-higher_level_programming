#!/usr/bin/python3
def uppercase(str):
    for y in str:
        x = ord(y)
        if x >= 97 and x <= 122:
            x -= 32
        print("{:c}".format(x), end="")
    print()
