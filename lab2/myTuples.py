#Example:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Example:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


#Example:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Example:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Example:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#Example:
tuple1 = ("abc", 34, True, 40, "male")


#Example:
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Example:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

'''             Access Tuple Items          '''

#Example:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Example:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Example:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


#Example:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


#Example:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Example:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#Example:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

'''                Update Tuples           '''

#Example:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Example:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Example:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Example:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


#Example:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

'''                     Unpack Tuples               '''

#Example:
fruits = ("apple", "banana", "cherry")


#Example:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Example:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Example:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


'''                     Loop Tuples             '''  

#Example:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Example:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Example:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


'''                 Join Tuples         '''

#Example:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Example:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

'''             Tuple Methods
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found               '''


#Exercise1:
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Exercise2:
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Exercise3:
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Exercise4:
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])