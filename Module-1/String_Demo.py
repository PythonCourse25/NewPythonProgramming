# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 13:09:48 2019

@author: Deepak
"""
#Three Ways to Create Python String
message='Hello CS4! How are you doing?'
message_New="Hello CS4! How are you doing?"
Message_Last='''Hello CS4! How are you doing?'''
print(message)
print(message_New)
print(Message_Last)
#Accessing individual character of the string
print(message[4])
#accessing the string character by negative referencing
print(message[-2],"\n",message_New[-8])
# working with broken string
#Example of Broken String
#print("Hello CS4,"How are you?"Let start Programming")
print('"Hello CS4,"Let we Start our Programming."Are You Ready?"')
demostr="Hello"
print(type(demostr))
#How Form Feed /f Works
#print('\x0c',end='')
print("\\f")
#string aligning
demostr2="{:>10}|{:<10}|{:>10}".format('hey','hi','hello')
print("Formatted String",demostr2)
#Formatting integer

