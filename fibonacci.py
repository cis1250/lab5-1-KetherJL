#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def fib(num):
    a = 0
    b = 1
    temp = 0
    if num < 0:
        print("Invalid input")
    elif num == 0:
        return 0
    elif num == 1:
        return b
    else:
        for i in range(num):
            print(a, end=" ")
            temp = a
            a = b
            b = temp + b

print(fib(5))
