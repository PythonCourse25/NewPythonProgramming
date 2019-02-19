#This program will delete the particular letter of the given index
Get_String=input("Please enter the string")
Get_Index=int(input("Please enter the index whose value need to be deleted from String"))
First_Part = Get_String[:Get_Index]
Second_Part = Get_String[Get_Index+1:]
Get_String = First_Part + Second_Part
if(Get_Index==-1):
    print(First_Part)
elif(Get_Index > len(Get_String)):
    print("Deletion is not Possible")
else:
    print("After removing the Nth index the string is",Get_String)

    