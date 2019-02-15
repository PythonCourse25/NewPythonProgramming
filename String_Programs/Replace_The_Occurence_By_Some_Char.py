# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:05:43 2019

@author: Deepak
"""
#Write a Python program to get a string from a given string where all 
#occurrences of its first char have been changed to '$', except the first char itself.
Get_string=input("Enter the String")
char= Get_string[0]
Get_string= Get_string.replace(char,'$')
Get_string = char + Get_string[1:]
print(Get_string)

