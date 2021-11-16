import math


def main():
    print("This program calculates the roots of a quadratic equation")
    a,b,c = eval(input("enter the coefficents a,b, and c: "))
    disc = math.pow(b, 2) - 4 * a * c
    if disc < 0:
        print('there are no real roots !')
    else:
        if disc == 0:
            root_disc = math.sqrt(disc)
            den = 2 * a
            root1 =(-b + root_disc) / den
            print('double root at', root1)
        else:
            root_disc = math.sqrt(disc)
            den = 2 * a
            root1 = (-b + root_disc) / den
            root2 = (+b + root_disc) / den
            print("the roots are", round(root1,2), round(root2, 2))

if __name__== '__main__'

def strategy_one():
    x1,x2,x3 = eval(input("enter three value"))
    max = 0
    if x1 >= x2 and x1>= x3
        max = x1
    elif x2 > =x1 and x2 >= 3
        max = x2
    else
        max = x3

    print("The largest value is", max)



def strategy_two():
    x1, x2, x3 = eval(input("enter three value"))
    max = x1
    if x2 > max:
        max = x2
    if x3 > max:
        max = x3
    my_list = (23,5,324,2,5,2,63,54,3,7)
    my_max = 0
    for number in my_list:
            if number > my_max:
                my_max = number
    print(my_max)


def main():
    try:
        print("This program calculates the roots of a quadratic equation")
        a, b, c = eval(input("enter the coefficents a,b, and c: "))
        disc = math.pow(b,2) - 4 * a * c
        root_disc =math.sqrt((disc))
        den = 2* a
        root1 = (-b +root_disc) / den
        root2 = (-b - root_disc) / den
        print("the roots are", round(root1,2), round(root2,2))
    except ValueError as exception_object
            if str(exception_object)== ' math domain error':
                print('no real roots')
            else:
                print(' did you enter three values ? ')
          except NameError:
            print(' make sure to enter all number')
          except SyntaxError:
            print(' did you put a comma ')
          except:









