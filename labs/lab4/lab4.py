"""
Name: <Belinda Trinh>
lab.py
"""
import math
from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", 400, 400)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to create new square")
    instructions.draw(win)
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # builds a rectangle
    # allows the user to click multiple times to build a new rectangle
    for i in range(num_clicks):
        user_click = win.getMouse()
        shape = Rectangle(Point(user_click.x - 10, user_click.y - 10), Point(user_click.x + 10, user_click.y + 10 ))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
    inst_pt = Point(width / 2, 10)
    instructions = Text(inst_pt, "Click again to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()

#
def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    width = 400
    height = 400
    win = GraphWin("Lab 4 Rectangles", width, height)

    point_1 = win.getMouse()
    point_2 = win.getMouse()
    rect = Rectangle(point_1, point_2)
    rect.setFill("blue")
    rect.draw(win)

    length = abs(point_2.getX() - point_1.getX())
    width = abs(point_2.getY() - point_1.getY())
    area = length * width
    perimeter = 2 * (length + width)
    txt = Text(Point(50,50)," The area is: " + str(area))
    txt.draw(win)
    txt = Text(Point(50,80)," The perimeter is : " + str(perimeter))
    txt.draw(win)



    win.getMouse()
    win.close()

def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4 Rectangles", width, height)
    point_1 = win.getMouse()
    point_2 = win.getMouse()

    x1 = point_1.getX()
    x2 = point_2.getX()
    y1 = point_1.getY()
    y2 = point_2.getY()
    radius= math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    c = Circle(point_1, r)
    c.draw(win)
    txt = Text(Point(50, 50), " The radius is : " + str(radius))
    txt.draw(win)

    win.getMouse()
    win.close()

def pi2():
    n = eval(input(" enter n:"))
    acc = 0
    for i in range (n):
        num = 4
        dem = 1 + 2 * i
        frac = (num/dem) * ((-1) ** i)
        acc = acc + frac
    print(acc)
    print(math.pi - acc)





def main():
    # squares()
     rectangle()
     #circle()
    # pi2()


main()
