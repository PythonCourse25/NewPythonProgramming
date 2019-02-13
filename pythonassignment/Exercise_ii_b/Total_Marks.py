# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:39:00 2019

@author: Deepak
"""
Theory_Marks=0
Practical_Marks=0
Percentage=0
Total_Marks=0
Marks_Obtained=input("Enter the 5 Subject Theory Marks and 3 Subjects Practical Marks Seperated by Comma Operator")
Segregated_Marks=Marks_Obtained.split(',')
print(Segregated_Marks)
Theory_Marks= (int(Segregated_Marks[0]) +int(Segregated_Marks[1]) +int(Segregated_Marks[2]) +int(Segregated_Marks[3]) +int(Segregated_Marks[4]))
Practical_Marks= int(int(Segregated_Marks[5]) +int(Segregated_Marks[6]) +int(Segregated_Marks[7]))
Total_Marks= Theory_Marks + Practical_Marks
Percentage= (Total_Marks*100)/500
print("The Total Marks Obtained by the User is=",Total_Marks)
print("The Percentage Obtained by the User is=",Percentage)
