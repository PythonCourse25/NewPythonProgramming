# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:26:57 2019

@author: Deepak
"""
String=input("Enter the Path of the File")
string = String.rsplit('/',1)
print("The name of the file with extension is",string[1])
