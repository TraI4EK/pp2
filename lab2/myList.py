#Example:
mylist = ["apple", "banana", "cherry"]

#Example:
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#Example:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#Example:
list1 = ["abc", 34, True, 40, "male"]

#Example:
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Example:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


'''                 Access List Items           '''
#Example:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Example:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Example:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Example:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


#Example:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


#Example:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Example:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


'''                     Change List Items           '''


#Example:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

'''             Add List Items          '''


#Example:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


'''             Remove List Items               '''

#Example:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Example:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#Example:
thislist = ["apple", "banana", "cherry"]
del thislist

#Example:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


'''             Loop Lists              '''


#Example:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Example:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


#Example:
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Example:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


'''                 List Comprehension              '''


#Example:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Example:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#Example:
newlist = [x for x in fruits if x != "apple"]


#Example:
newlist = [x for x in fruits]

#Example:
newlist = [x for x in range(10)]

#Example:
newlist = [x for x in range(10) if x < 5]

#Example:
newlist = [x.upper() for x in fruits]


#Example:
newlist = ['hello' for x in fruits]

#Example:
newlist = [x if x != "banana" else "orange" for x in fruits]


'''                 Sort Lists              '''


#Example:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Example:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Example:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Example:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Example:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Example:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Example:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Example:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

'''                 Copy Lists              '''

#Example:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Example:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


'''                 Join Lists              '''

#Example:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Example:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Example:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


#Exercise1:
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Exercise2:
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)

#Exercise3:
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#Exercise4:
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)

#Exercise5:
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

#Exercise6:
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Exercise7:
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Exercise8:
fruits = ["apple", "banana", "cherry"]
print(len(fruits))