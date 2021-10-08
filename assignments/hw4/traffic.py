

def main():
    number_of_roads = int(input(" how many roads were surveyed? :"))
    total_vehicles = 0
    for road in range(1, number_of_roads + 1):
        number_of_days = int(input(" how many days was road "+str(road) + " surveyed ?"))
        acc = 0
        for day in range(1, number_of_days + 1):
            cars_per_day = int(input("how many cars travelled on day "+str(day)+"?"))
            acc = acc + cars_per_day
        average_cars = acc / number_of_days
        print(" Road", road, "average vehicles per day:", round(average_cars, 2))
        total_vehicles = acc + total_vehicles
    average_vehicles = total_vehicles/ number_of_roads
    print("Total number of vehicles traveled on all roads :", total_vehicles)
    print("Average number of vehicles per road:", round(average_vehicles, 2))
if __name__ == '__main__':
    main()
