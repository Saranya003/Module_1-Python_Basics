#A parameter is a variable listed inside the parantheses in the func definition
def myFunc1(x,y):
    print(x+" "+y)
#Argument is a value that is sent to the function when it is called
myFunc1("Hello","World!")

#Passing List as a argument
List=["Accord","Audi A6","Mercedes C Class","Pajero Sport","Endeavour"]
def myFunc2(x):
    print(x*2)
myFunc2(List)

#passing function as argument

def myFunc3(y):
    return y.upper()

def myFunc4(y):
    return y.lower()

def myFunc5(z):
    var=z("I am Salman")
    print(var)

myFunc5(myFunc3)
myFunc5(myFunc4)