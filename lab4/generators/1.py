def squareNum(stop):
    i = 0
    while i <= stop:
        yield i**2
        i += 1

num = list(squareNum(int(input())))
print(num)