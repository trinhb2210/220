def calc_area() :
    length = 20
    width = 5
    area = length * width
    print("Area =", area)
def calc_area() :
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width"))
    height = eval(input("Enter the height"))
    volume = length * width * height
    print("Volume=", volume)
def shooting_percentage():
    total = eval(input("Enter the total shots: "))
    made = eval(input("Enter the shots made: "))
    percentage = made/total * 100
    print(" percentage=", percentage)
def coffee():
    pounds = eval(input("Enter the number of pounds: "))
    total = 10.50 * pounds + .86 * pounds + 1.50
    print(" total=", total)
def kilometers_to_miles():
    numbers = eval(input( "Enter the numbers of kilometer he travels: "))
    miles =  numbers / 1.61
    print(" miles=", miles)
