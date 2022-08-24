num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
operations = input("Choose the operations to perform(+,-,*,/)")
if operations=="+":
    num3=num1+num2
elif operations=="-":
    num3=num1-num2
elif operations=="*":
    num3=num1*num2
elif operations=="/":
    num3=num1/num2
else:
    print("illegal operator")
print(num3)