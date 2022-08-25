num = int(input("Enter the number : "))
length_Of_Number = len(str(num))
print(length_Of_Number)
armnum = 0
temp=num
while temp>0:
    digit = temp%10
    armnum = armnum+digit**length_Of_Number
    temp=temp//10
if(num==armnum):
    print("the number is armstrong")
else:
    print("the number is not armstrong")
