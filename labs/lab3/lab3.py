"""
Name: <Belinda Trinh>
<lab3>.py
Certification of Authenticity
I certify that this assignment is entirely my own work
"""
def average():
    acc=0
    x = eval(input("How many homeworks did you have?: "))
    for i in range(1, x + 1):
        score = eval(input("Enter your grade on HW" + str(i) + ":"))
        acc=acc+score
    acc=acc/x
    print(acc)
#
def tip_jar():
    acc=0
    for i in range (0,5):
        x = eval(input("how much do you want to tip ?:"))
        acc=acc+x
    print(acc)

def newton():
    x = eval(input(" enter the number x:"))
    refine= eval(input("how many times do you want to refine it ?: "))
    acc= x/2
    for i in range(refine):
        acc = acc + x/acc / 2
    print(acc)

def sequence():
    x= eval(input("enter the number of terms "))
    for x in range (1,x+1):
        y=1+(x // 2 * 2)
        print(y, end="")
def pi():
    n= eval(input("enter the number of terms "))
    acc=1
    for x in range (n ):
        num= 2+(x//2*2)
        dem= 1+((x+1)//2 *2)
        acc=acc*(num/dem)
    print(acc)








