# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 06:08:09 2019

@author: Deepak
"""
#set flag to False assumig item is not in the list
shopping=[]
flag=False
#maximum elements user want to insert in the list
count=int(input("How many elements you want to insert in the list?"))
#input from user
print("Please insert the item in the list:")
for i in range(count):
    num=input("Enter The lements in List")
    shopping.append(num)
#displaying the list item
print("The items in the list is as follows:")
for i in range(count):
    print(shopping[i])
#asking from user what item he wants to search?
item=input("Please insert the item to be search in the list")
#Apply Linear Search to find the element in the list
for i in range(count):
    if(item==shopping[i]):
        flag=True
        print("Item found at index",i)
if (flag==False):
    print("Item is not present in the list")
        
