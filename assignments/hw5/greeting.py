"""
Name : Belinda Trinh
greeting.py
Problem: Write a program that displays a heart
Certification of Authenticity
I certify that this assignment is entirely my own work

"""
from time import sleep
from graphics import *

def main():
    win = GraphWin("Greeting Card",700, 500)
    txt = Text(Point(350, 50), "Happy Valentine's day !")
    txt.setSize(30)
    txt.draw(win)
    heart1 = Circle(Point(280,175), 60)
    heart1.setOutline('pink')
    heart1.setFill('pink')
    heart2 = Circle(Point(390,175), 60)
    heart2.setOutline('pink')
    heart2.setFill('pink')
    heart1.draw(win)
    heart2.draw(win)
    triangle = Polygon(Point(445,200), Point(330,400), Point(225, 200))
    triangle.setFill('pink')
    triangle.setOutline('pink')
    triangle.draw(win)
    aline = Line(Point(400, 300), Point(180, 230))
    aline.setArrow("first")
    aline.draw(win)
    for i in range(50):
        aline.move(9,3)
        sleep(0.1)

    instructions = Text(Point(350, 450), "Click anywhere to close")
    instructions.draw(win)
    win.setBackground("red")
    click = win.getMouse()
    win.close(click)
if __name__ == '__main__':
    main()
