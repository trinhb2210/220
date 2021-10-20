"""
Name : Belinda Trinh
vigenere.py
Problem: Write a program that encode a message.
Certification of Authenticity
I certify that this assignment is entirely my own work

"""
from graphics import *
def code( message, keyword):
    msg = message
    word = keyword
    word = word.upper()
    msg = msg.upper()
    msg = msg.split(" ")
    word = word.split(" ")
    msg = "".join(msg)
    word = "".join(word)
    acc = ""
    for i in range(len(msg)):
        c = msg[i]
        key = word[i]

def main():
    win = GraphWin("Vigenere", 400, 400)
    win.setBackground(color_rgb(255,255,255))

    message = Text(Point(50,70), " Message to code")
    message.draw(win)
    keyword = Text(Point(45,110), " Enter Keyword ")
    keyword.draw(win)
    input_box1 = Entry(Point(200,70),25)
    input_box1.draw(win)
    input_box2= Entry(Point(200, 110), 25)
    input_box2.draw(win)
    button = Text(Point(170, 170), " Encode")
    button.draw(win)
    aRectangle = Rectangle(Point(120,150), Point(220,190))
    aRectangle.draw(win)

    win.getMouse()

    message = input_box1.getText()
    keyword = input_box2.getText()

    aRectangle.undraw()

    button.setText("Resulting message")
    encoded_message = Text(Point(200,250), code(message, keyword))
    encoded_message.draw(win)

    close = Text(Point(200,350), " Click anywhere to close window")
    close.draw(win)
    win.getMouse()
    win.close()

main()


