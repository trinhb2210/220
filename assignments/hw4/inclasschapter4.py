#def initials():
    first = input("please enter your first name ( all lowercase): ")
    last = input("please enter your last name ( all lower case): ")
    first_initial = first[0]
    last_seven=last [0:7]
    uname= first_initial + last_seven
    print(uname)
    print(first[0] + last [:7])

#def get_month(pos):
    index = (pos -1 ) * 3
    months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
    month_abbrev = months[months[index:index +3]
    print('Month', pos, 'is ' + month_abbrev )

def encode ( message):
    for s in message:
        x= ord(s)
        print(x, end="")

