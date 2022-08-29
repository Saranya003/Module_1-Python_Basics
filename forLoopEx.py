'''
Syntax:
for value in sequence:
    loop body
'''
# Looping through string
name="Salmeera"
for letters in name:
    print(letters)

# Looping through string
fruits=["Maambazham", "VaazhaiPazham", "Sappotta", "Kamala Orange","Maathulai"]
for x in fruits:
    print(x)
# break statement
#fruits=["Maambazham", "VaazhaiPazham", "Sappotta", "Kamala Orange","Maathulai"]
for y in fruits:
    print(y)
    if y=="VaazhaiPazham":
        break
# continue statement
for z in fruits:
    if z=="Sappotta":
        print(z)
        continue
#range function
for i in range(4):
    print(i)
    #print('I am Legend')
for i in range(7,11):
    print(i)
for i in range(12,30,4): # third value increments of i
    print(i)

# else in for loop
for i in range(4):
    print(i)
else:
    print("Success")

# Nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement
for x in [0,1,2]:
    pass
