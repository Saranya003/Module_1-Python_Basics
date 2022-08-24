# Unordered, Changeable and do not duplicate values
# can store heterogeneous items
# declared within {curly braces}
# dict is a keyword

dict_1 = {"Name":"Salman",
          "Age":29,
          "Gender":'FeMale',
          "DOB":"Aug 22, 1993",
          "Weight":85.5,
          "Gender":'Male',
          "Height":173,
          "isAvailable":True,
          "Likes":["Cricket","Music","Movies","Python"]}
print(dict_1)
print(len(dict_1))

# To access the item in the dict declare a new variable

x = dict_1["Name"]
print(x)
# also
y = dict_1.get("Age")
print(y)
# to change the value of the key
dict_1["DOB"] = "22-08-1993"
print(dict_1)
# also
dict_1.update({"Height":169})
print(dict_1)
# Add new items in dict
dict_1["Colour"]="Black"
print(dict_1)
# Remove an item
dict_1.pop("Gender")
print(dict_1)
# To get only the keys
print(dict_1.keys())
# To get only the Values
print(dict_1.values())