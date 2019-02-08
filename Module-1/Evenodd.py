def Evenodd(x):
    if x%2 == 0:
        print(x,"is Even")
    else:
        print(x,"is Odd")
def get_data():
    n=int(input("Enter the number to be checked?"))
    Evenodd(n)
get_data()