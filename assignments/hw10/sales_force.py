"""
Name : Belinda Trinh
sales_force.py
Problem: Write a program that creates a class that encapsulates data for a salesperson.
Certification of Authenticity
I certify that this assignment is entirely my own work

"""
from sales_person import SalesPerson


class SalesForce(SalesPerson):
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        with open(file_name) as f:
            lines = f.readlines()
        for line in lines:
            employee_id, name, sale_amounts = line.split(",")
            this_sale_person = SalesPerson(int(employee_id), name)
            for sale in sale_amounts.split():
                this_sale_person.enter_sale(float(sale))
            self.sales_people.append(this_sale_person)

    def quota_report(self, quota):
        result = []
        for person in self.sales_people:
            temp = [
                person.employee_id, person.name,
                person.total_sales(),
                person.met_quota(quota)
            ]
            result.append(temp)

        return result

    def top_seller(self):
        highest_dict = dict()
        for person in self.sales_people:
            if person.total_sales() in highest_dict:
                highest_dict[person.total_sales()].append(person)
            else:
                highest_dict[person.total_sales()] = [person]
        sorted_dict = sorted(highest_dict, reverse=True)
        return highest_dict[sorted_dict[0]]

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if str(employee_id) == str(person.employee_id):
                return person
        return None
