#Method/Funtion is a block of code which only will run when you call for it
def testfunc1():
    print("This is Salman")
testfunc1()  # Calling the function
# Passing a single argument / paramaterized method
def testfunc2(lname):
    print("Mohamed "+lname)
x="Ibrahim"
y="Salman"
testfunc2(x)
testfunc2(y)

# Passing a single argument / paramaterized method
def testfunc3(x,y):
    print(x+" "+y)
a="Salman"
testfunc3(a,"Chennai!")
b="Salm"
c="eera"
testfunc3(b,c)

# Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement
def myfunction():
  pass
