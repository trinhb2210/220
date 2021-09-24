"""
Name : Belinda Trinh
calculate.py
Problem: This program calculates the monthly interest charge
Certification of Authenticity
I certify that this assignment is entirely my own work

"""


def main():
    interest = float(input("Enter the annual interest rate:"))
    days = eval(input("Enter the number of days in the billing cycle: "))
    previous_balance = eval(input("Enter the previous (net) balance: "))
    payment = eval(input("Enter the payment amount: "))
    payment_day = eval(input("Enter the day of the billing cycle in which the payment made: "))

    amount1 = previous_balance * days
    amount2 = payment * (days - payment_day)
    balance = amount1 - amount2
    average_daily_balance = balance / days

    monthly_interest_rate = interest/12 * (1/100)
    monthly_interest_charges = average_daily_balance * monthly_interest_rate
    print(round(monthly_interest_charges, 2 ))
if __name__ == '__main__':

    main()
