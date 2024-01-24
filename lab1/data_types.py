#Example
x = 5
print(type(x))

#Example
x = "Hello World"	#str	
x = 20	            #int	
x = 20.5	        #float	
x = 1j	            #complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	                    #range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	                #bool	
x = b"Hello"	            #bytes	
x = bytearray(5)	        #bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	                #NoneType




#Example -If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World")	        #str	
x = int(20)	                    #int	
x = float(20.5)	                #float	
x = complex(1j)	                #complex	
x = list(("apple", "banana", "cherry"))	        #list	
x = tuple(("apple", "banana", "cherry"))	    #tuple	
x = range(6)	                                #range	
x = dict(name="John", age=36)	                #dict	
x = set(("apple", "banana", "cherry"))	        #set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	                #bool	
x = bytes(5)	            #bytes	
x = bytearray(5)	        #bytearray	
x = memoryview(bytes(5))	#memoryview


#Exercise1:

x = 5
print(type(x))
#It would print int data type of x.

#Exercise2:
x = "Hello World"
print(type(x))
#It would print string data type of x.

#Exercise3:
x = 20.5
print(type(x))
#It would print float data type of x.

#Exercise4:
x = ["apple", "banana", "cherry"]
print(type(x))
#It would print list data type of x.

#Exercise5:
x = ("apple", "banana", "cherry")
print(type(x))
#It would print tuple data type of x.

#Exercise6:
x = {"name" : "John", "age" : 36}
print(type(x))
#It would print dict data type of x.

#Exercise7: 
x = True
print(type(x))
#It would print bool data type of x.