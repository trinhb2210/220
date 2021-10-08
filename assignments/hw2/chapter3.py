""""
Name : Belinda Trinh
chapter4.py
Problem: a place to play with chapter 4 material
Certification of Authenticity
I certify that this assignment is entirely my own work

"""

from graphics import *

win = GraphWin("My Window",700, 500)

pointA = Point(350, 250)
pointB = Point(100, 50)

circleA = Circle(pointA, 50)
circleB = Circle(pointA, 50)

pointA.draw(win)
pointB.draw(win)

circleA.draw(win)
circleA = Circle(pointA, 50)
circleA.setFill("red")
circleB.move(200, 0)
print("Cirlce A: ", circleA)
print("Circle B: ", circleB)

circleA.draw(win)
circleB.draw(win)

win.getMouse()