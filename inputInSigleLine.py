'''x,y,z=input("Enter three numbers : ").split()
if (x>y and x>z):
    print("The greatest number is : ",x)
elif (y>x and y>z):
    print("The greatest number is : ",y)
else:
    print("The greatest number is : ",z)'''


# Single variable and multiple input
value=list(map(int,input("Enter the numbers : ").split(' ')))
print(*value)

    