# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 01:23:46 2019

@author: Deepak
"""
#initialize variables
Sum=a=b=c=d=0
#welcome message
print("Welcome to Medha Innovation")
print("First Assignment Programs")
print("We will calculate the sum of 5-digit number")
# User Input a number
number = int(input("Requesting user to enter 5-digit number"))
# Finding the sum of individual digits 
a= number%10
number = int(number/10)
b= number %10
number = int(number/10)
c= number %10
number = int(number/10)
d= number %10
number = int(number/10)
Sum = number + a + b + c + d
print("The sum of individual digit of 5-digit number is", Sum)
