# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:15:45 2019

@author: Deepak
"""
String=input("Enter the Path of the File")
string = String.rsplit('.',1)
print("The Extension of the Fileis",string[1])
