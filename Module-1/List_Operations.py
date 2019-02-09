# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 10:29:20 2019

@author: Deepak
"""
shopping=[]
flag=False
print("Welcome CS4 Second Year, Today We will see all the operations on List")
while(True):
    print("Press 1 to create a list")
    print("Press 2 to insert an element in a list")
    print("Press 3 to change the element of list")
    print("Press 4 to remove or delete the element from list")
    print("Press 5 to search the element in the list")
    print("Press 6 to display the elements of the list")
    print("Press 7 to exit from the program")
    choice=int(input("Please enter your choice")) 
    if(choice==1):
        number= int(input("How many numbers you want to insert in the list"))
        for i in range(number):
            num=int(input())
            shopping.append(num)
        print("The List is successfully created")
    if(choice==2):
        position=int(input("Please specify the position where you want to insert an element in list"))
        num=int(input("Please enter the number"))
        shopping.insert(position,num)
        print("The Number is inserted in the List")
    if(choice==3):
        position=int(input("Please specify the position where you want to change an element in list"))
        if(len(shopping)<position):
            print("Sorry Position specify by the user is out of range")
        else:
            num=int(input("Please enter the number"))
            shopping[position]=num
            print("The element in the list has been changed successfully")
    if(choice==4):
        number=int(input("Please specify the position where you want to delete an element from list"))
        shopping.remove(number)
        print("The element has been removed from the list")
    if(choice==5):
        item=int(input("Please insert the item to be search in the list"))
        for i in range(len(shopping)):
            if(item==shopping[i]):
                flag=True
                print("Item found at index",i)
                break
            else:
                flag= False
        if (flag==False):
            print("Item is not present in the list")
    if(choice==6):
        print("Elements present in the list are as follows:")
        for item in shopping:
            print(item)
    if(choice==7):
        break
                
   