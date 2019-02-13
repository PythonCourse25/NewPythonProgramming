# -*- coding: utf-8 -*-
"""
Created on: Tue Feb 12 18:43:17 2019
@author: Anidhya Bhatnagar
@description: Program for Use Case - II A
"""

# Taking input from the user
s_no = 1
part_number = input("Enter Part Number: ")
part_description = input("Enter Part Decription: ")
quantity = int(input("Enter quantity sold: "))
price = int(input("Enter price of item: "))

# Calculating the invoice amount
invoice_amount = quantity * price

# Printing / Displaying the Invoice
print("|" + "-" * 78 + "|")
print("|" + " " * 28 + "PYTHON HARDWARE STORES" + " " * 28 + "|")
print("|" + "-" * 78 + "|")
print("| S. No. |   Part No   |        Part Name        | Quantity | Price |  Amount  |")
print("|" + "-" * 78 + "|")
print("|{:^8}|{:^13}|{:25}|{:10}|{:7}|{:10}|".format(s_no, part_number, part_description, quantity, price, invoice_amount))
print("|" + " " * 8 + "|" + " " * 13 + "|" + " " * 25 + "|" + " " * 10 + "|" + " " * 7 + "|" + " " * 10 + "|")
print("|" + " " * 8 + "|" + " " * 13 + "|" + " " * 25 + "|" + " " * 10 + "|" + " " * 7 + "|" + " " * 10 + "|")
print("|" + " " * 8 + "|" + " " * 13 + "|" + " " * 25 + "|" + " " * 10 + "|" + " " * 7 + "|" + " " * 10 + "|")
print("|" + " " * 8 + "|" + " " * 13 + "|" + " " * 25 + "|" + " " * 10 + "|" + " " * 7 + "|" + " " * 10 + "|")
print("|" + " " * 8 + "|" + " " * 13 + "|" + " " * 25 + "|" + " " * 10 + "|" + " " * 7 + "|" + " " * 10 + "|")
print("|" + " " * 8 + "|" + " " * 13 + "|" + " " * 25 + "|" + " " * 10 + "|" + " " * 7 + "|" + " " * 10 + "|")
print("|" + "-" * 78 + "|")
print("|" + " " * 78 + "|")
print("|" + " " * 78 + "|")
print("|" + " " * 69 + "SIGNATURE|")
print("|" + "-" * 78 + "|")

