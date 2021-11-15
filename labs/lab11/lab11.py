"""
Name: Belinda Trinh
lab11.py
"""
def words(ifn):
    infile = open(ifn,"r")
    contents = infile.read()
    return contents.split("\n")

def random_word (list):
    return list[randint(0,len(list) -1)]
def fill(word,letters):
    secret = ["_"].len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)
def won (word, letters):
    x = fill(word, letters)
    if word == x :
        return True
    else:
        return False

def play():
    w = words("words.txt")
    secret = random_word(w)
    incorrect = 0
    current = "_".len(secret)
    guesses = []
    while incorrect < 7 and not :
        display = fill (secret, guesses )
        print (display)
        print(guesses)
        letter = input(" What is the letter ?")
        while letter in guesses:
            letter = input(" What is the letter?")
        guesses.append(letter)
        display = fill(secret, guesses)
        if current != display :
            incorrect+= 1
        else:
            current = display



