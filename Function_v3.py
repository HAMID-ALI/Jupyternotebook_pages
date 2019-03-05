def to_hour(mins, second=0):
    hrs=mins/60+second/3600
    return hrs
m=int(input("Enter vale of mins: "))
print("Your time in hours is "+str(to_hour(m)))
print("Your time in hours plus 1 hr is"+str(to_hour(m)+1))
sec=int(input("Enter vale of secs: "))
print("Your time in hours is "+str(to_hour(m,sec)))
print("Your time in hours plus 1hr is "+str(to_hour(m,sec)+1.0))