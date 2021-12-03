"""
Name : Belinda Trinh
sales_person.py
Problem: Write a program that creates a class that encapsulates data for a salesperson.
Certification of Authenticity
I certify that this assignment is entirely my own work

"""
class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        elif self.total_sales() > other.total_sales():
            return 1
        else:
            return 0

    def __str__(self):
        return f"{self.employee_id}-{self.name}: {self.total_sales}"
