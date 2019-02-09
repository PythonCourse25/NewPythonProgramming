#initialize the variables
lname=fname=gender=name=''
#Printing The Welcome Message
print("Welcome to Cafe Coffee Shop\n")
print("Please provide your following Information\n")
#Information of the user
lname=input("Please tell me your last Name.....")
fname=input("Please tell me your firsat name")
gender=input("Please tell me your gender")
name=input("Tell /me to whom you want to meet?")
#printing the waiting message to the user
if(gender=="male" or gender=="Male" or gender=="MALE"):
    print("Please take your seat Mr. {}{}. Mr. {} is busy in meeting till then please take a cup of coffee.". format(fname,lname, name))
else:
    print("Please take your seat Ms. {}{}. Mr. {} is busy in meeting till then please take a cup of coffee.". format(fname,lname, name))
