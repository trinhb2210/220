"""
Name : Belinda Trinh
hello.py
Problem: print Hello,world! to the screen
Certification of Authenticity
I certify that this assignment is entirely my own work

"""
import math

def main():
    print("This program calculates the root of a quadratic equation")
    print()

    a, b, c = eval(input("enter the coefficient og the quadratic function: "))
    disc_root = math.sqrt(b ** 2 - 4 * a * c)
    root1 = (-b + disc_root) / (2 * a)
    root2 = (-b - disc_root) / (2 * a)

    print("the roots are", root1, root2)

if __name__=='__main__':
    main()


    def main():
        print("This calculates thr factorial of a number")
        print()

        num = eval(input("enter a number: "))
        acc = 1
        for i in range(num, 1, -1):
            acc = acc * num

        print(acc)