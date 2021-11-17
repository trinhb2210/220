"""
Name : Belinda Trinh
three_door_game.py
Problem: Write a program that creates three button games.
Certification of Authenticity
I certify that this assignment is entirely my own work

"""
from graphics import *
import random
from button import Button



def main():
    win = GraphWin("Three Button Game", 500, 500)
    # First text
    text1 = Text(Point(250, 20), "I have a secret door")
    text1.draw(win)
    # Second test
    text2 = Text(Point(250, 300), "Click to choose my door")
    text2.draw(win)
    # First button
    shape1 = Rectangle(Point(20, 70), Point(100, 150))
    button1 = Button(shape1, "Door1")
    button1.draw(win)
    # Second button
    shape2 = Rectangle(Point(120, 70), Point(200, 150))
    button2 = Button(shape2, "Door2")
    button2.draw(win)
    # Third button
    shape3 = Rectangle(Point(220, 70), Point(300, 150))
    button3 = Button(shape3, "Door3")
    button3.draw(win)
    # create a random door
    secret_door = random.randint(1, 3)
    # User click coordinate
    point = win.getMouse()
    # Check button clicked
    if button1.is_clicked(point) == True and secret_door == 1:
        button1.color_button("green")
        text1.setText("You Win")
        text2.setText("Click to close")
    elif button2.is_clicked(point) == True and secret_door == 2:
        button2.color_button("green")
        text1.setText("You Win")
    elif button3.is_clicked(point) == True and secret_door == 3:
        button3.color_button("green")
        text1.setText("You Win")
    else:
        text1.setText("You Lost!")
        text2.setText(f"Door{secret_door} is my secret door")
        if button1.is_clicked(point) == True:
            button1.color_button("red")
        if button2.is_clicked(point) == True:
            button2.color_button("red")
        if button3.is_clicked(point) == True:
            button3.color_button("red")

if __name__ == "__main__":
    main()
