"""
Name : Belinda Trinh
convert.py
Problem: convert C to F
Certification of Authenticity
I certify that this assignment is entirely my own work

"""
import math
def main():
    acc = 0
    x = eval(input("Number of values to be entered: "))
    for i in range(1, x + 1):
        y = eval(input("Enter your value: "))
        acc = acc + (y * y)
    mean = float(acc) / x
    rms_average = math.sqrt(mean)
    print(round(rms_average, 3))


    for i in range(1, x +1):
        y = eval(input("Enter your value: "))
        acc = acc + (1 / y)
    harmonic_mean = x / acc
    print(round(harmonic_mean,3))

    acc=1
    for i in range(1,x +1):
        y = eval(input("Enter your value: "))
        acc = acc * y
    geometric_mean= math.pow(acc, 1/x)
    print(round(geometric_mean,3))


