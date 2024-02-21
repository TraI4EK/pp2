def toZero(start):
    while start >= 0:
        yield start
        start -= 1

num = list(toZero(15))

print(num)