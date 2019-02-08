#initialize the variables
lname=fname=gender=name=''
print("Welcome to Cafe Coffee Shop\n")
print("Please provide your following Information\n")
lname=input("Please tell me your last Name.....")
fname=input("Please tell me your firsat name")
gender=input("Please tell me your gender")
name=input("Tell /me to whom you want to meet?")
print("Please take your seat Mr. {}{}. Mr. {} is busy in meeting till then please take a cup of coffee.". format(fname,lname, name))