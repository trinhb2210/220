import math
"""
Name: <Belinda Trinh>
<Lab 2>.py
"""
def sum_of_threes():
    acc=0
    a=eval(input("enter the max"))
    for x in range (0,a+1,3) :
        acc= acc+x
    print(acc)
#
def muliplication_table():
    for h in range (1,11):
        for l in range (1,11):
            print(h*l,end=" ")
        print()
#
def triangle_area():
    a=eval(input("enter side 1"))
    b=eval(input("enetr side 2"))
    c=eval(input("enter side 3"))
    s= (a+b+c)/2
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(A)
#
def sumSquares():
    start=eval(input("enter starting number"))
    end=eval(input("enter ending number"))
    acc=0
    for x in range (start,end +1 ):
        acc+=(x*x )
    print(acc)
#
def power():
    base=eval(input("enter the base"))
    exponent=eval(input("enter the exponent"))
    acc=1
    for x in range (exponent):
        acc=acc*base
    print(acc)









