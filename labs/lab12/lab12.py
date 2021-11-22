"""
Name: Belinda Trinh
lab12.py
"""


def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Belinda"
    except:
        pass

def readdata(int):
    f= open( int,"r")
    data = f.read()
    data = data.split()
    return data
def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == i :
            return True
        i+= 1
    return False
def good_input():
    x = eval(input(" Enter a number in the range 1 to 10:")
    while x < 1 or x > 10:
        x = eval(input( "Enter the number again : "))
        return x
def num_digits():
    num = eval(input("Enter the a positive number:")
    while num >= 1 :
        digits = 0
        while num!= 0:
            num // = 10
            digits += 1
        print(digits)
        num = eval(" Enter the number again:")

from random import randint
def high_low_game():
    secret = randint(1,100)
    guess = 0
    num = eval(input("Guess a number:"))
    while num != secret and guess < 7:
        guess = guess + 1
        if num < secret :
            print(" Your number is too low")
        else:
            print(" Your number is too high")
        num = eval(input(" Guess another number: "))
    if num == secret :
        print(" You win in " + str(guess) + " guesses")
    else:
        print(f"Sorry You lose. The number is {secret} ")

