#Example:Create a Class
class MyClass:
  x = 5
#Example:Create Object
p1 = MyClass()
print(p1.x)

#Example: The __init__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#Example:The __str__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)


#Example:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#Example: Object Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#Example:The self Parameter
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Example: Modify Object Properties
p1.age = 40


#Example: Delete Object Properties

del p1.age
#Example:Delete Objects

del p1
#Example:
class Person:
  pass

#Exercise1:
class MyClass:
  x = 5

#Exercise2:
class MyClass:
  x = 5
p1 = MyClass()
#Exercise3:
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)
#Exercise4:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age