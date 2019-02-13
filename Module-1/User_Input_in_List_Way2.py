# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 04:15:25 2019

@author: Deepak
"""

def Insert_into_List():
    
    element= int(input("How many Elements you want to insert in List"))
    list_Element=[None for _ in range(element)]
    for i in range(element):
        list_Element[i]=int(input())
    for item in list_Element:
        print(item)
#Driver Code
Insert_into_List()