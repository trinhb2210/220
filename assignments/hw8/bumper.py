"""
Name : Belinda Trinh
bumper.py
Problem: Write a program that creates two circles moving in random direction.
Certification of Authenticity
I certify that this assignment is entirely my own work

"""
from random import randint
import math
from graphics import *


def delay(d):
    for i in range(d):
        for i in range(1000):
            pass


def get_random(move_amt):
    return randint(min(-move_amt, move_amt), max(-move_amt,move_amt))


def get_random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def did_collide(cir1, cir2):
    p1 = cir1.getCenter()
    p2 = cir2.getCenter()
    r1 = cir1.getRadius()
    r2 = cir2.getRadius()
    if math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2) <= r1 + r2:
        return True
    else:
        return False


def hit_vertical(cir, win):
    p = cir.getCenter()
    r = cir.getRadius()
    h = win.getHeight()
    w = win.getWidth()
    if (p.getY()) >= h or (p.getY()) <= 0.0:
        return True
    elif (p.getX() + r) >= w or (p.getX() - r) <= 0:
        return True
    else:
        return False


def hit_horizontal(cir, win):
    p = cir.getCenter()
    r = cir.getRadius()
    w = win.getWidth()
    h = win.getHeight()
    if (p.getX()) >= w or (p.getX()) <= 0:
        return True
    elif (p.getY() + r) >= h or (p.getY() - r) <= 0.0:
        return True
    else:
        return False


def main():
    win = GraphWin("Bumper World", 500, 500)
    win.setBackground('black')
    cir1 = Circle(Point(250, 250), 50)
    cir2 = Circle(Point(100, 100), 50)


    cir1.setFill(color_rgb(*get_random_color()))
    cir1.draw(win)

    cir2.setFill(color_rgb(*get_random_color()))
    cir2.draw(win)

    p1 = cir1.getCenter()
    p2 = cir2.getCenter()

    move_amount = 5
    cir1_dx = get_random(move_amount)
    cir1_dy = get_random(move_amount)
    cir2_dx = get_random(move_amount)
    cir2_dy = get_random(move_amount)
    keepGoing = True
    while True:
        d = 400
        delay(d)

        # First circle
        cir1.move(cir1_dx, cir1_dy)
        # Second circle
        cir2.move(cir2_dx, cir2_dy)

        # Check collision
        if did_collide(cir1, cir2):
            cir1_dx = -cir1_dx
            cir1_dy = -cir1_dy
            cir2_dx = -cir2_dx
            cir2_dy = -cir2_dy

        # check boundary, see if it hit the wall
        if hit_horizontal(cir1, win):
            cir1_dx = -cir1_dx
        if hit_vertical(cir1, win):
            cir1_dy = -cir1_dy

        if hit_horizontal(cir2, win):
            cir2_dx = -cir2_dx
        if hit_vertical(cir2, win):
            cir2_dy = -cir2_dy


if __name__ == "__main__":
    main()
