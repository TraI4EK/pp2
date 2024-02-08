import math
def filter_prime(numbers : str) -> list:
    splitted_list = [int(x) for x in numbers]
    is_prime = lambda n: all(n % i != 0 for i in range(2, int(n /2) + 1))
    return list(filter(is_prime, splitted_list))

x = input().split()

print(filter_prime(x))