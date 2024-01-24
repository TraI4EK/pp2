#Example
x = 5
y = "John"
print(x)
print(y)

#Example
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Example
x = 5
y = "John"
print(type(x))
print(type(y))

#Example
x = "John"
# is the same as
x = 'John'

#Example
a = 4
A = "Sally"
#A will not overwrite a

'''                     Variables Names                     '''

#Example
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Example - Illegal variable names:
'''2myvar = "John"
my-var = "John"
my var = "John"'''
#Example - Each word, except the first, starts with a capital letter:
myVariableName = "John"

#Example - my_variable_name = "John"
my_variable_name = "John"

'''                 Assign Multiple Values                      '''

#Example
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Example - This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

'''                 Output variavle                  '''

#Example
x = "Python is awesome"
print(x)

#Example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Example
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Example
x = 5
y = 10
print(x + y)

#Example
x = 5
y = "John"
print(x + y)

#Example
x = 5
y = "John"
print(x, y)

'''             Global Variables            '''


#Example
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Example
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#Example
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#Exercise1:

carname = "Volvo"

#Exercise2:
x =50

#Exercise3:
x = 5
y = 10
print(x+y)

#Exercise4:
x = 5
y = 10
z = x+y
print(z)

#Exercise5:
x,y,z = "Orange", "Banana", "Cherry"

#Exercise6:
x = y = z = "Orange"

#Exercise7:
def myfunc():
  global x
  x = "fantastic"