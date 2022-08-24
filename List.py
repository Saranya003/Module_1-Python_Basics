# stores mutiple data in a single variable
# can store heterogeneous items
# Ordered, Changeable and allow duplicates
# declared within [sq. brackets]

List=["Salman",29,'Male',82.5,["Accord",97]]
print(List)
print(len(List))
print(type(List))
print(List[1])
print(List[1:5])  # prints from index[1] to index[4]
print(List[2:])  # prints from index[2] to end
print(List[:3])  # prints from beginning to index[2]
List[1]="Vayasu aayiruchu kumaru"
print(List)
List[1:3]=[29,"Aambala Maama - Evlo kevalamana piravi illa?"]
print(List)
# Add item in certain position
List.insert(3,"Iraivi")
print(List)
List.insert(3,"Male")
# Adds item at the end of the list
List.append("Jigarthanda")
print(List)
# Remove item
List.remove("Iraivi")
print(List)
# find the index position
print(List.index("Jigarthanda"))
