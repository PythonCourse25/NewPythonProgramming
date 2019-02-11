# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 03:29:01 2019

@author: Deepak
"""
Final_Number=a=b=c=d=0
#welcome message
print("Welcome to Medha Innovation")
print("First Assignment Programs")
print("We will reverse the 5-digit number")
# User Input a number
number = int(input("Requesting user to enter 5-digit number"))
# Finding the reverse of 5-digits number
a= number%10
a=a+1
a=a%10
number = int(number/10)
b= number %10
b=b+1
b=b%10
number = int(number/10)
c= number %10
c=c+1
c=c%10
number = int(number/10)
d= number %10
d=d+1
d=d%10
number = int(number/10)
number = number + 1
number= number%10
Final19991_Number=number*10000+d*1000+c*100+ b*10+a
print("After adding 1 to the individual digit of 5-digit number", Final_Number)
