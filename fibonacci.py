#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def fib(num):
    a = 0
    b = 1
    temp = 0
    for i in range(num):
        print(a, end=" ")
        temp = a
        a = b
        b = temp + b

def user():
    while True:
        user_input = input("Enter an integer: ")
        if user_input.strip().isdigit():
            return int(user_input)
        else:
            print("That's not a valid integer. Please try again.")

def make_fib():
    n = user()
    fib(n)

make_fib()
