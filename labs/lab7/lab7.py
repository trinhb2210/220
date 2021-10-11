"""
Name: <Belinda Trinh>
Partner: <your partner's name goes here – first and last>
<lab7>.py
"""
import math

def cash_conversion():
    i = eval(input(" Enter the integer : "))
    print("${:.2f}".format(i))
def encode():
    x = input("integer key value")
    k = eval(input(" enter message to be encoded :  "))
    acc = ""
    for c in x:
        i = ord(c)
        new_character = chr(i + k)
        acc = acc + new_character
    print(acc)

def sphere_area(radius):
    return ( 4 * math.pi * radius ** 3)
def sphere_volume(radius):
    return((4/3) * math.pi * radius ** 3)
def sum_n(n):
    acc = 0
    for i in range (1, n +1):
        acc+= i
    return acc
def sum_n_cubes(n):
    acc = 0
    for i in range(1, n+1):
        acc+= i * i * i
    return acc
def encode_better():
    m = input(" message to be encoded : ")
    n = input(" enter the cipher key: ")
    acc = ""
    for i in range(len(m)):
        c = ord(m[i])
        key =ord(k[i])
        acc+=chr(c + key)
        print(acc)








def main():
    cash_conversion()
    print(sphere_area(5))
    print(sphere_volume(2))
    print(sum_n(10))
    print(sum_n_cubes(10))
    encode()

main()