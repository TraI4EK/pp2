#Example:
a = 33
b = 200
if b > a:
  print("b is greater than a")
#Example:
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error

#Example:
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Example:
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Example:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Example:
if a > b: print("a is greater than b")


#Example:
a = 2
b = 330
print("A") if a > b else print("B")

#Example:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Example:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#Example:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Example:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Example:
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#Example:
a = 33
b = 200

if b > a:
  pass

#Exercise1:
a = 50 
b = 10
if a >b:
  print("Hellow world")
#Exercise2:
a = 50
b = 10
if a !=b:
  print("Hello World")

#Exercise3:
a = 50 
b = 10
if a == b:
  print("Yes")
else:
  print("No")

#Exercise4:
a = 50
b = 10
if a ==b: 
 print("1")
elif a >b:
 print("2")
else:
  print("3") 
#Exercise5:
if a == b and c == d:
  print("Hello")

#Exercise6:
if a == b or c == d:
  print("Hello")

#Exercise7:
if 5 > 2:
    print("YES")

#Exercise8:
a = 2
b = 5
print("YES") if a == b else print("NO")
#Exercise9:
a = 2
b = 50
c = 2
if a == c or b == c:
 print("YES")
