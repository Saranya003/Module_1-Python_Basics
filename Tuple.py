# stores mutiple data in a single variable
# can store heterogeneous items
# Ordered, UnChangeable and allow duplicates
# declared within (parantheses)
# tuple is a keyword

Tuple = ("Sameera",'Female',26,65.2,["Biriyani","Shawarma"],"Iraivi")
print(Tuple)
print(len(Tuple))
print(Tuple[4])
print(type(Tuple))
print(Tuple[1:5]) # prints from index[1] to index[4]
print(Tuple[2:]) # prints from index[2] to end
print(Tuple[:3]) # prints from beginning to index[2]

# we cannot append or insert an item, as tuple is unchangeable
# to append or insert we need to convert tuple to list, do the neccessary things and convert to tuple
x=list(Tuple)
print(x)
x.insert(1,"Salman")
x.append(97)
print(x)
y=tuple(x)
print(y)