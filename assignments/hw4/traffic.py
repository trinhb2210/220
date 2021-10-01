"""
Name : Belinda Trinh
traffic.py
Problem: This program calculates the
I certify that this assignment is entirely my own work

"""


def main():
    roads = eval(input(" how many roads were surveyed? :"))
    total_vehicles = 0
    for road in range(1, roads + 1):
        number = eval(input(" how many days was road "+str(road) + " surveyed ?"))
        acc = 0
        for day in range(1, number + 1):
            cars_per_day = eval(input("how many cars travelled on day" + str(day) + ":"))
            acc = acc + cars_per_day
        avg = acc/ number
        print(" Road", road, "average vehicles per day", round(avg, 2))
        total_vehicles = acc + total_vehicles
    average_vehicles = total_vehicles/ roads
    print("Total number of vehicles traveled on all roads : ", total_vehicles)
    print("Average number of vehicles per road:", round(average_vehicles,2))


