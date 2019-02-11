# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 04:05:39 2019

@author: Deepak
"""
#initialize variables
reverse_number=a=b=c=d=0
#welcome message
print("Welcome to Medha Innovation")
print("First Assignment Programs")
print("We will reverse the 5-digit number")
# User Input a number
number = int(input("Requesting user to enter 5-digit number"))
# Finding the reverse of 5-digits number
a= number%10
number = int(number/10)
b= number %10
number = int(number/10)
c= number %10
number = int(number/10)
d= number %10
number = int(number/10)
reverse_number = number + a*10000 + b*1000 + c*100 + d*10
print("The sum of individual digit of 5-digit number is", reverse_number)
