"""
Name : Belinda Trinh
weighted_average.py
Problem: Write a program that calculates the weighted average.
Certification of Authenticity
I certify that this assignment is entirely my own work

"""
def weighted_average(in_file_name, out_file_name):
    input_file = open(in_file_name, "r")
    lines = input_file.readlines()

    output_file = open(out_file_name, "w")

    class_average = 0
    counter = 0

    for line in lines:
        full_name, number = line.split(":")
        numbers_list = number.split(" ")
        numbers_list.pop(0)
        weight_acc = 0
        average_acc = 0
        for i in range(len(numbers_list)):
            # Even number divided by 2, remainder = 0
            # % = mod
            if i % 2 == 0:
                weight_acc = weight_acc + int(numbers_list[i])
            else:
                average_acc = average_acc + int(numbers_list[i]) * int(numbers_list[i - 1])
        if weight_acc < 100:
            output_file.write(f"{full_name}'s average: Error: The weights are less than 100. \n")
        elif weight_acc > 100:
            output_file.write(f"{full_name}'s average: Error: The weights are more than 100. \n")
        else:
            counter = counter + 1
            rounded_average = round(average_acc / 100, 1)
            output_file.write(f"{full_name}'s average: {rounded_average} \n")
            class_average = class_average + average_acc/100

    output_file.write(f"Class average: {round(class_average / counter, 1)}")

    input_file.close()
    output_file.close()


def main():
    in_file_name = "grades.txt"
    out_file_name = "avg.txt"
    weighted_average(in_file_name, out_file_name)


if __name__ == "__main__":
    main()
