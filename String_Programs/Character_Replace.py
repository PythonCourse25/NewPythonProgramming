# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:12:20 2019

@author: Deepak
"""
Get_string1=input("Enter the First String")
Get_string2=input("Enter the second string")
Get_String3=''
Get_string4= Get_string1[:len(Get_string1)-1]+Get_string2[-1]
Get_string5=Get_string2[:len(Get_string2)-1] +Get_string1[-1]
Get_string3 = Get_string4 +','+Get_string5
print(Get_string3)

