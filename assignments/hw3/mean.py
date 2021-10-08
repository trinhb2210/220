"""
Name : Belinda Trinh
mean.py
Problem: This program calculates the root-mean-square , the harmonic mean and the geometric mean
I certify that this assignment is entirely my own work

"""
import math


def main():
    rms_acc = 0
    harmonic_acc = 0
    geometric_acc = 1
    number = eval(input("Number of values to be entered: "))
    for i in range(1, number + 1):
        value = eval(input("Enter your value: "))
        rms_acc = rms_acc + (value * value)
        harmonic_acc = harmonic_acc + (1 / value)
        geometric_acc = geometric_acc * value
    mean = float(rms_acc) / number
    rms_average = math.sqrt(mean)
    harmonic_mean = number / harmonic_acc
    geometric_mean = math.pow(geometric_acc, 1 / number)
    print(round(rms_average, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))


if __name__ == '__main__':

    main()



