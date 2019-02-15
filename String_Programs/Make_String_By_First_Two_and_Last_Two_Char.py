# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 23:08:01 2019

@author: Deepak
"""
#Write a Python program to get a string made of the first 2 
#and the last 2 chars from a given a string. If the string 
#length is less than 2, return instead of the empty string.
Get_string=input("Enter the String")
print(Get_string[:2]+Get_string[-2:])
