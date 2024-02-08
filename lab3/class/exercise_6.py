class Solution:
    def __init__(self, numbers : list):
        self.numbers = numbers

    def prime_number_filter(self) -> list:
        is_prime = lambda n: all(n % i != 0 for i in range(2, int(n/2) + 1))
        self.numbers = [num for num in self.numbers if is_prime(num)]
        return self.numbers
    
   
s = Solution([1, 2, 3, 4, 5, 18, 19, 21, 25, 131])

print(s.prime_number_filter())

    