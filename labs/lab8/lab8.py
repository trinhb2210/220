"""
Name: Belinda Trinh
lab8.py
"""
def encode_better():
    msg = input(" message to be encoded : ")
    key = input(" enter the cipher key: ")
    acc = ""
    for i in range(len(msg)):
        c = ord(msg[i])
        key =ord(key[i])
        acc+=chr(c + key)
        return acc

def encode(msg,key):
    key = input("integer key value")
    msg = eval(input(" enter message to be encoded :  "))
    acc = ""
    for c in msg:
        i = ord(c)
        new_character = chr(i + key)
        acc = acc + new_character
    return acc

def count_word(infile_name, outfile_name):
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(str(i) + " " + word + "\n")
            i+=1
    infile.close()
    outfile.close()

def hour_wage(infile_name, outfile_name):
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w+")
    for line in infile:
        acc = ""
        parts = line.split()
        wage = float(parts[2])
        wage += 1.65
        acc+= parts[0]
        acc+= parts[1]
        weekly_wage= wage * int(parts[3])
        acc+= str(weekly_wage)
        outfile.write(acc + "\n" )

def isbn(isbn_str):
    acc= 0
    for i in range(10):
        pos = 10 - i
        acc+= int(isbn_str[i]) * pos
    return acc

def send_message(file,friend):
    infile= open(file,"r")
    outfile=open(friend + ".txt","w+")
    for line in infile:
        outfile.write(line)
def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        encode(line)
        outfile.write(line)
    # add other function calls here
def send_uncrackable_message(file, friend, pad):
    pad_file = open(pad,"r")
    key = pad_file.read()
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        encode_beter(line,key)
        outfile.write(line)



def main():
    count_word("Walrus.txt", "count.txt")
    hour_wage("hourly_wages.txt", "new_pay2.txt")
