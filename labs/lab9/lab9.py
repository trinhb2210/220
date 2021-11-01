"""
Name: Belinda Trinh
lab9.py
"""
from graphics import *
import math
def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
def listSum(nums):
    acc = 0
    for i in range(len(nums)):
        acc+= nums[i]
    return acc
def returnNumbers(strNums):
    for i in range(len(strNums)):
        strNums[i] = float(strNums[i])
def writeSumofSquares():
    infile = input("What files are the numbers in ?:" )
    outfile = input("Name of output file")
    readfile = Open(infile,"r")
    writefile = Open(outfile,"w")
    for line in infile:
        nums = line.split()
        returnNumbers(nums)
        squareEach(nums)
        s = listSum(nums)
        writefile.write("Sum of Square =" + str(s))

def starter():
    weight = float(input("player'weight:")
    numWins= int(input("the number of wins the player has had :"))
    if  weight >= 150 and weight < 160:
        print(" You're a right fit for this position ")
    elif numWins >=5:
        print(" You're a right fit for this position ")
    else:
        print("Sorry, You are not a good fit for this position")

    if weight > 199:
        print(" You're a right fit for this position ")
    elif numWins > 20:
        print(" You're a right fit for this position ")
    else:
        print("Sorry, You are not a good fit for this position")


def main():
    nums = [5, 2, -3]
    addTen(nums)
    squareEach(nums)
    print(nums)
    s = listSum(nums)
    print(s)
    strNums = ["3","5.7","2"]
    returnNumbers(strNums)
    writeSumofSquares()



