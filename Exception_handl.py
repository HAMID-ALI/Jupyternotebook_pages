def divide(a,b):
    try:
        return(a/b)
    except:
        print("Division by zero not defined")
a=4
b=int(input("Enter vale of b"))
divide(a,b)