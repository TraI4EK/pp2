def cnt_letters(word):
    up_case = 0
    low_case = 0

    for letter in word:
        if letter.isupper():
            up_case += 1
        else:
            low_case += 1
    return up_case, low_case

word = input()

upper, lower = cnt_letters(word)

print(f"The number of upper case letters is {upper}\nThe number of lower case letters is {lower}")