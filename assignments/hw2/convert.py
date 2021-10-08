"""
Name : Belinda Trinh
convert.py
Problem: convert C to F
Certification of Authenticity
I certify that this assignment is entirely my own work

"""
# 0 -> 32
# 100 -> 212
# identifiers
# start with a letter or
def main():
    celsius = eval(input("please enter the temperature in celsius"))# take user input in degrees celsius and call it celsius
    fahrenheit=  9 / 5 * celsius + 32# convert input to fahrenheit using the equation (9 / 5) x celsius + 32
    print("Hey, that's" ,fahrenheit, "degrees fahrenheit!" )# print the output as degrees fahrenheit
    main()


