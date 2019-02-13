# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:56:13 2019

@author: Deepak
"""
Title= "Python Hardware Shop"
S_No=1
Part_Number=input("Enter the Part Number")
Part_Name=input("Enter the name of Hardware")
Quantity= int(input("Enter the Quantity to be purchased"))
Price= float(input("Enter the price of an item"))
Invoice_Amount= Quantity * Price
Sub_Total = Invoice_Amount
GST = .1*Sub_Total
Shipping= .05* Sub_Total
Total = Sub_Total + GST + Shipping
print("|" + "-" *78 + "|")
print("|" + " "*78 + "|")
print("|" +"{:^78}".format(Title) + "|")
print("|" + "-" *78 + "|")
print("|{:^8}|{:^13}|{:^14}|{:^16}|{:^12}|{:^10}|" .format("S.No", "Part No.", "Part Name", "Quantity","Price","Amount"))
print("|" + "-"*78 + "|")
print("|{:^8}|{:^13}|{:^14}|{:^16}|{:^12}|{:^10}|" .format(S_No,Part_Number,Part_Name,Quantity,Price,Invoice_Amount))
print("|" + " "*8 +"|" + " "*13 + "|" + " "*14 + "|" + " "*16 + "|" + " "*12 + "|" + " "*10 + "|")
print("|" + " "*8 +"|" + " "*13 + "|" + " "*14 + "|" + " "*16 + "|" + " "*12 + "|" + " "*10 + "|")
print("|" + " "*8 +"|" + " "*13 + "|" + " "*14 + "|" + " "*16 + "|" + " "*12 + "|" + " "*10 + "|")
print("|" + " "*8 +"|" + " "*13 + "|" + " "*14 + "|" + " "*16 + "|" + " "*12 + "|" + " "*10 + "|")
print("|" + " "*8 +"|" + " "*13 + "|" + " "*14 + "|" + " "*16 + "|" + " "*12 + "|" + " "*10 + "|")
print("|" + " "*8 +"|" + " "*13 + "|" + " "*14 + "|" + " "*16 + "|" + " "*12 + "|" + " "*10 + "|")
print("|" + " "*8 +"|" + " "*13 + "|" + " "*14 + "|" + " "*16 + "|" + " "*12 + "|" + " "*10 + "|")
print("|" + " "*8 +"|" + " "*13 + "|" + " "*14 + "|" + " "*16 + "|" + " "*12 + "|" + " "*10 + "|")
print("|" + " "*8 +"|" + " "*13 + "|" + " "*14 + "|" + " "*16 + "|" + " "*12 + "|" + " "*10 + "|")
print("|" + " "*8 +"|" + " "*13 + "|" + " "*14 + "|" + " "*16 + "|" + " "*12 + "|" + " "*10 + "|")
print("|" + "-" *78 + "|")
print("{:>68}".format("SubTotal") + "|" + "{:^10}".format(Sub_Total) + "|")
print(" " *68 + "-"*12)
print("{:>68}".format("GST 10.000%") + "|" + "{:^10}".format(GST) + "|")
print(" " *68 + "-"*12)
print("{:>68}".format("Shipping and Handling 5.000%") + "|" + "{:^10}".format(Shipping) + "|")
print(" " *68 + "-"*12)
print("{:>68}".format("Total") + "|" + "{:^9} ".format(Total) + "|")
print(" " *68 + "-"*12)
print(" " + " " *78 + " ")
print(" " + " " *78 + " ")
print(" " + " " *78 + " ")
print(" " + " " *78 + " ")
print(" " + "-" *78 + " ")
print("|" + " "*78 + "|")
print("|" + " "*78 + "|")
print("|" + " "*78 + "|")
print("|""{:>78}".format("SIGNATURE") + "|")
print(" " + "-" *78 + " ")
