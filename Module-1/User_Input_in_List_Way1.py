# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 04:15:25 2019

@author: Deepak
"""

def Insert_into_List():
    list_Element=[]
    element= int(input("How many Elements you want to insert in List"))
    for i in range(element):
        list_Element.append(int(input()))
    for item in list_Element:
        print(item)
#Driver Code
Insert_into_List()