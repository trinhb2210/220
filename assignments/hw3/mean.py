"""
Name : Belinda Trinh
mean.py
Problem: This program calculates the root-mean-square , the harmonic mean and the geometric mean
I certify that this assignment is entirely my own work

"""
import math


def main():
    n = eval(input("Number of values to be entered: "))
    for i in range(1, n + 1):
        y = eval(input("Enter your value: "))
    acc = 0
    for i in range(0, n - 1 + 1,1):
        acc = acc + (y * y)
    mean = float(acc) / n
    rms_average = math.sqrt(mean)
    print(round(rms_average, 3))

    acc=0
    for n in range(1, n+1):
        acc = acc + (1 / y)
    harmonic_mean = float(n) / acc
    print(round(harmonic_mean,3))



