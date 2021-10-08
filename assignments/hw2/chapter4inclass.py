from graphics import *
def main():
    win = GraphWin("Celsius Converter", 500, 500)
    win.setCoords(0, 0 , 10, 10)

    celsius_temp_text = Text(Point(3, 9), "Celsius Temperature: ")
    celsius_temp_text.draw(win)

    user_input = Entry(Point(7,9),5)
    user_input.draw(win)

    convert_text= Text(Point(5,5), "Convert It")
    button_outline = Rectangle(Point(3,6), Point(7,4))
    convert_text.draw(win)
    button_outline.draw(win)

    output_label = Text(Point(3, 1), "Fahrenheit Temperature")
    output_label.draw(win)

    output_value = Text(Point(7,1), "")
    output_value.draw(win)

    win.getMouse()

    celsius_temp= eval(user_input.getText())

    fahrenheit_temp=(9.0/5.0) * celsius_temp +32

    output_texf.setText(fahrenheit_temp)

    win.getMouse()

if __name__== '__main__':