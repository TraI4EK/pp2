x = "great"

def func1():
    print("KBTU is", x)

def func2():
    x = "awesome"
    print("KBTU is", x)

func1()
func2()
func1()

ourlist = [1, 2 ,3 ]
print (ourlist[-1])
print (ourlist)

a, b, c = ourlist

print(a, b, c)

ourstr = "sebum"

'''print(ourstr[0])

print(ourstr[-1])
print(ourstr[len(ourstr)-1])
print(ourstr[ : -1])
'''
for i in range(0, len(ourstr)):
    print(ourstr[i])