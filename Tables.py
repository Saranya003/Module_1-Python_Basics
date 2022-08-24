TableNumber=int(input("Enter the table number : "))
Count=int(input("The table should be executed until : "))
for i in range(1,Count+1):
    table = TableNumber*i
    print(table)