def option_one():
    file_name= input('Enter the filename : ')
    in_file = open(file_name, 'r')
    data = in_file.read()
    print(data)
    in_file.close()
