# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 23:58:52 2019

@author: Deepak
"""
#To insert and delete the data in list
List=[]
while(1):
    print("1 to insert the data at the end of the list")
    print("2 to insert the data at specific position")
    print("3 to delete the data from the end of the list")
    print("4 to deletet the data from any specific position")
    print("5 to display the data of the list")
    print("Please enter your choice")
    choice=int(input("Please enter your choice"))
    if(choice==1):
        num=int(input("Enter the number to be inserted in the list"))
        List.append(num)
    if(choice==2):
        num=int(input("Enter the number to be inserted in the list"))
        position=int(input("Please enter the position where you want to insert your data"))
        if(position>len(List)):
            print("Sorry Data can not be inserted Try Again")
        else:
            List.insert(position,num)
    if(choice==5):
        for item in List:
            print(item)
    if(choice>5):
        break
    
