def evenNum(stop):
    i = 0
    while i <= stop:
        if i % 3 == 0 and i % 4 == 0:
            yield i
        i += 1

num = list(evenNum(int(input())))

print(", ".join(map(str, num)))