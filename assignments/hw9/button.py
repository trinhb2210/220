"""
Name : Belinda Trinh
button.py
Problem: Write a program that creates three button games.
Certification of Authenticity
I certify that this assignment is entirely my own work

"""
from graphics import *
class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.p1 = self.shape.getP1()
        self.p2 = self.shape.getP2()
        x1 = self.p1.getX()
        x2 = self.p2.getX()
        y1 = self.p1.getY()
        y2 = self.p2.getY()
        x = (x2 + x1) // 2
        y = (y2 + y1) // 2
        self.text = Text(Point(x, y), label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.text.draw(win)
        self.shape.draw(win)

    def undraw(self):
        self.text.undraw()
        self.shape.undraw()

    def is_clicked(self, point):
        x = point.getX()
        y = point.getY()
        x1 = self.p1.getX()
        x2 = self.p2.getX()
        y1 = self.p1.getY()
        y2 = self.p2.getY()
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
        else:
            return False

    def color_button(self, color):
        # setter function
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)

