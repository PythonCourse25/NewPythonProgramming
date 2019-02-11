# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 04:16:51 2019

@author: Deepak
"""
answer=number=bits_to_be_shift=0
print("Welcome user, Today we will see how leftshift operator works")
print("Left Shift is a bit wise operator which works on bits")
print("Left shift means remove bits from the left and append that much 0's in the right")
print("The formula to perform Left shift operation is number * 2 raise to power bits_to_be_shift")
print("Now let we take input a Number")
number = int(input("Now i request you to input a number"))
print("Now we will enter how many bits we want to shift of that number")
bits_to_be_shift=int(input("Again i request you to enter the number that tell to the computer how many bits to be shift"))
print("Now when we apply leftshift operator the result will be stored in answer variable")
answer = number<<bits_to_be_shift
print("After performing the operation the result is",answer)
print("Ohhh Confused how it happens?")
print("Now let us understand it by taking example")
print("When we enter any decimal number the computer stored it in 8-bit or 16-bit or 32-bit format dependes on the length")
print("Suppose we have entered 5 the binary value of 5 is 00000101")
print("Now look at the number left most bit is known as most significant bit and right most is known as least significan bit")
print("When 1 is moving towards most significant bit the result will increase in power of 2")
print("Suppose we have entered a number whose bit need to be shift is 5")
print("and then we enter another number that represent how many bits need to be shift i.e 2")
print("The two bits from the left will be discarded and two zeros from the right will be append")
print("Then the number looks like 00010100")
print("Now the decimal value of this number is 20")
print("That what we will get in our output")
print("I think now its bit clear to you")
print("Thank you have a great day")
