x=int(input("Enter the length of the side 1: "))
y=int(input("Enter the length of the side 2: "))
z=int(input("Enter the length of the side 3: "))
if ((x+y)>z and (x+z)>y and (y+z)>x):
    print("The triangle can be printed")
else:
    print("The triangle can't be printed")