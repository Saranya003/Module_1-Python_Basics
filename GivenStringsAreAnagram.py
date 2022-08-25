str_1 = input("Enter the first string : ")
str_2 = input("Enter the second string : ")
str_1.lower()
str_2.lower()
len_1 = len(str_1)
len_2= len(str_2)
if (len_1==len_2):
    sorted_1 = sorted(str_1)
    sorted_2 = sorted(str_2)
    if(sorted_1==sorted_2):
        print("The given strings are an anagram")
    else:
        print("The given strings are not an anagram")
else:
    print("The given strings are not anagram")
