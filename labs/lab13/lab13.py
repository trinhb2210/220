"""
Name: Belinda Trinh
lab13.py
"""

def binary(list, value):
    mid = list[len(list)//2]
    while mid != value and len(list) != 1:
        if mid > value:
            list = list[:]
        else:
            list = list[:]
        mid = list[len(list)//2]
    if len(list) == 1 and list[0] != value:
        return False
    else:
        return True

def selection_sort(values):
    for i in range (len(values)):
        lowest = values [i]
        pos = i
        for j in range ( i + 1, len(values)):
            if values[j] < values[lowest]:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


main()
