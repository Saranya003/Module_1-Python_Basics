def palindrome():
    gvn_num = int(input("Enter the number : "))
    pal_num = 0
    temp = gvn_num
    while temp>0:
        digit = temp%10
        power=len(str(temp))
        pal_num = pal_num+(digit)*10**(power-1)
        temp=temp//10
    print(pal_num)
palindrome()
