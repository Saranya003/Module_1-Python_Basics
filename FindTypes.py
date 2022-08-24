x=15
y=5.99
z=8j
print((type(x)))
print((type(y)))
print((type(z)))

#converting the data types
#int to float
a=float(x)
print("Int to float : ", a)
#float to int
b= int(y)
print("Float to int : ",b)
#int to complex
c= complex(x)
print("Int to complex : ",c)
#float to complex
d=complex(y)
print("Float to complex : ",d)

"""
#complex to int
e=int(z)
print("Complex to int : ",e)
#complex to float
f=float(z)
print("Complex to float : ",f)
"""

# we cannot perform complex to int/float operations