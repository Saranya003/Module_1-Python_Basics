num=int(input("Enter the number : "))
if (num>1):
    for i in range (2,num//2+1):
        if (num%i==0):
            print("The number is not a prime number")
            break
        else:
            print("The number is a prime number!!")
            break
else:
    print("The number is not a prime number")