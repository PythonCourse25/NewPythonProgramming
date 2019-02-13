# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:02:44 2019

@author: Deepak
"""
Theory_Marks=0
Practical_Marks=0
Percentage=0
Total_Marks=0
Marks_Obtained=input("Enter the 5 Subject Theory Marks and 3 Subjects Practical Marks Seperated by Comma Operator")
Segregated_Marks=Marks_Obtained.split(',')
print(Segregated_Marks)
Theory_Marks= (int(Segregated_Marks[1]) +int(Segregated_Marks[2]) +int(Segregated_Marks[3]) +int(Segregated_Marks[4]) +int(Segregated_Marks[5]))
Practical_Marks= int(int(Segregated_Marks[6]) +int(Segregated_Marks[7]) +int(Segregated_Marks[8]))
Total_Marks= Theory_Marks + Practical_Marks
Percentage= (Total_Marks*100)/440
print(Segregated_Marks[0], "Obtained", Theory_Marks,"Marks out of 350 and", Practical_Marks,"Marks out of 90 in Practicaland Succesfully Passed the Exampe with",Percentage,"% in aggregate. Many Many Congratulation to",Segregated_Marks[0] )
