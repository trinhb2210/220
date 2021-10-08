def encode( message):
    for ch in message:
        x = ord(ch)
        print(x, end=" ")

def decode (message):
    num_list = message.split()
    acc = ''
    for num in num_list:
        acc = acc + chr(eval(num))
        print(acc)
def parse_data(date):
    months = [' January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October', 'November', 'December']
    month_string, day_string, year_string = date.split('/')
    month_int = int(month_string)
    day_int = int(day_string)
def happy():
    print('happy Birthday to you')
#scope- where the variable can be reference. The variable "name" can only be used within the body of the function.
# name is local to def sing. Scope is restricted to only that function.
def sing(name):
    happy()
    happy()
    print('Happy Birthday dear ' + name + '!')
    happy()
def sing_fred():
    happy()
    happy()
    print('Happy birthday dear Fred')
    happy()

def sing_lucy():
    happy()
    happy()
    print('happy birthday dear Lucy')
    happy()

def main():
    #caller
    sing('Fred') #argument is 'Fred'
    sing_fred()
    print()
    sing_lucy()
    print()
    sing_fred()

if __name__ == '__main__':
    #called /invoked
    main()