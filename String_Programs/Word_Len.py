# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:36:10 2019

@author: Deepak
"""
Word_Len=[]
Longest_Word_Len=[]
Element=int(input("How many Elements you want to insert?"))
for i in range(Element):    
    Word_Len.append(input("Enter the String"))
for item in Word_Len:
    Longest_Word_Len.append(len(item))
Longest_Word_Len.sort(reverse=True)
print("The Longest Word Length=",Longest_Word_Len[0])
