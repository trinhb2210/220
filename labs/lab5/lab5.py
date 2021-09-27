"""
Name: <Belinda Trinh>
lab5.py
"""
import math

from graphics import *

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target


    # Wait for another click to exit
    win.getMouse()
    win.close()


#def triangle():
    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    # Wait for another click to exit
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)
    point_1 = win.getMouse()
    point_2 = win.getMouse()
    point_3 = win.getMouse()

    s1 = Line(point_1, point_2)
    s2 = Line(point_2, point_3)
    s3 = Line(point_3, point_1)
    aPolygon = Polygon(point_1, point_2, point_3)
    aPolygon.draw(win)
    p1 = abs(point_2.getX() - point_1.getX())
    p2 = abs(point_2.getY() - point_1.getY())
    L1 = math.sqrt(p1 **2 + p2 ** 2)
    p3 = abs(point_3.getX() - point_2.getX())
    p2 = abs(point_3.getY() - point_2.getY())
    L2 = math.sqrt(p3 **2 + p2 **2)
    p1 = abs(point_3.getX() - point_1.getX())
    P3 = abs(point_3.getY() - point_1.getY())
    L3 = math.sqrt(p1 **2 + p3 **2)

    perimeter = L1 + L2 + L3
    s = perimeter / 2
    area = math.sqrt(s - L1)*(s - L2) * (s - L3)
    txt = Text(Point(100, 90), " The area is: " + str(area))
    txt.draw(win)
    txt = Text(Point(100, 120), " The perimeter is : " + str(perimeter))
    txt.draw(win)


    win.getMouse()
    win.close()


#def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    blue_box = Entry(Point(250,300), 3)
    red_box = Entry(Point(250,310), 3)
    green_box = Entry(Point(250,340), 3)
    blue_box.draw(win)
    red_box.draw(win)
    green_box.draw(win)
    win.getMouse()
    for i in range(5):
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)
        win.getMouse()

    # Wait for another click to exit
    win.getMouse()
    win.close()
def process_string():
    s = input(" Enter text")
    first = s[0]
    last = s[-1]
    t = s[2:5]
    concatentation =[0] + [-1]
    repetition = s[0:3] * 10
    numbers = (len(s))
    for i in range(len(s)):
        print(s[i])
    print(first)
    print(last)
    print(t)
    print(concatentation)
    print(repetition)
    print(numbers)
def another_series():
    n =eval (input("number of terms"))
    acc =0
    for i in range (n):
        y = 2 +(2 * 3%)
        print(y)



def main():
    # target()
    #triangle()
     #color_shape()
     #process_string()
    another_series()


main()
