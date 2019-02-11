#Welcome CS4 Second Year, Today We will see what operations we can perform on string
# Definition of Capitalizing String
def string_capitalize(getstring):
    getstring=getstring.capitalize()
    return(getstring)
#Definition for string Casefold
def string_length(getstring):
    
    getstring=len(getstring)
    return(getstring)
def string_reverse(getstring):
    print("The copy String",getstring)
    rev_str = ''
    rev_str = reversed(getstring)
    return(rev_str)
def main_menu():
    string = input("Enter your string")
    while(1):
        print("press 1 to capitlize the string")
        print("press 2 to find length the string")
        print("press 3 to reverse the string")
        print("press 4 to check string is pallindrme or not")
        print("Press 5 to Exit from the program")
        choice=int(input("Please enter your choice to perform operation on string"))
        if(choice==1):
            str1=string_capitalize(string)
            print("String after Capitalizing",str1)
        if(choice==2):
            str1=string_length(string)
            print("The Length of the String is=",str1)
        if(choice==3):
            str1=string_reverse(string)
            print("The reverse sring is",list(str1))
        if(choice==4):
            rev_str=''
            string=string.casefold()
            rev_str = reversed(string)
            if(list(string)==list(rev_str)):
                print("Pallindrome")
            else:
                print("Not Pallindrome")
        if(choice==5):
            break

main_menu()
    
        