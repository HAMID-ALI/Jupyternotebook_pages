def divide(a,b):
    try:
        return(a/b)
    except:
        return("Division by zero not defined")
a=4
b=int(input("Enter vale of b "))
print(divide(a,b))
print("End of program")