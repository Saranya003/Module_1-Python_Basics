x=int(input("Enter the 1st number : "))
y=int(input("Enter the 2nd number : "))
z=int(input("Enter the 3rd number : "))
if (x>y and x>z):
    print("The greatest number is : ",x)
elif (y>x and y>z):
    print("The greatest number is : ",y)
else:
    print("The greatest number is : ",z)