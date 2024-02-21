def squares(start, stop):
    while start <= stop:
        yield start**2
        start += 1

num = list(squares(10, 20))
print(num)

x = []
for i in range(10, 21):

    x.append(i**2)

print(x)    