# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:12:44 2019

@author: Deepak
"""

#Shopping List Example
shopping=["Bread","Butter","Chocklates"]
print(shopping)
#Printing the List using Loop
for item in shopping:
    print(item)
#Add item in the end of the list
shopping.append("Oil")
print(shopping)
shopping.insert(0, "Gas")
print(shopping)
for i in range(len(shopping)):
    print(shopping[i])

