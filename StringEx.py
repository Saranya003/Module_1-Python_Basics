#anything withing the single, double and triple quotes
name = "Salman"
x='''thi is 
the multiline
string example''' #for multiline string we need to write withing triple quotes

#String python is basically an array
#python does not have char datatype

name = "Salman"
print(name[2])
print(len(name))

y = "I am Salman and I a legend!"
print("legend!" in y)
print("leg" in y)
print("legpiece" in y)

#Slice the string
y = "I am Salman and I am a legend!"
print(y[5:11])
print(y[:11])
print(y[12:])

#to upper and lower case
print(y.upper())
print(y.lower())

#Remove spaces
z="     Salmeera    "
print(z)
print(z.strip())

#Replace
a="Hello, Chennai!"
b=a.replace("e","Y")
print(b)
#Split
c=a.split(" ")
print(c)
#Concat
d="vanakkam"
e=a+d
print(e)
#Capitalize
print(d.capitalize())
#casefold
print(d.casefold())

#Escape characters
print("We are \"VIKINGS\" of the north")

#sort
sortedWord = sorted(d)
print(sortedWord)

