from itertools import permutations

def all_permutations(string_ : str) :
    permutations_of_the_string = permutations(string_)
    permutated_string = list(permutations_of_the_string)
    permutated_string = [''.join(permutation) for permutation in permutated_string]
    for i in permutated_string:
        print(i)

    return None

all_permutations("abc")
