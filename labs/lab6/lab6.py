"""
Name: <Belinda Trinh>
lab 6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    first_name = input("Please enter your first name : ")
    last_name = input(" Please enter your last name : ")
    print(last_name,",", first_name)

def company_name():
    name = input("Please enter the three-part internet domain name : ")
    x = name.split(".")
    print(x[1])

def initial():
    x = eval(input(" how many names will be input ? :"))
    for i in range(1, x + 1):
        first_name = input("Enter the first name of student " + str(i) + ":")
        last_name = input(" Enter last name: ")
        print(first_name[0] + last_name[0])

def names():
    names = input(" Enter a list of name:")
    names = names.split(", ")
    for x in names:
        first_name = x.split(" ")[0]
        last_name = x.split(" ")[1]
        print(first_name[0] + last_name[0])

def third():
    n = eval(input(" how many sentences will be input : "))
    for i in range(1, n + 1):
        sentence = input(" Please enter the sentence :")
        print(sentence[2::3])

def word_average():
    acc = 0
    sentence = input(" Please enter the sentence: ")
    x = sentence.split(" ")
    for word in sentence:
        acc+= len(word)
        avg = acc/len(x)
    print(avg)









def main():
    #name_reverse()
    #company_name()
    #initial()
    #names()
    #third
    word_average

main()
