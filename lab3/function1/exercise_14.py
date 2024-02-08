def uniqPlays():
    from exercise_13 import Guess_the_number
    from exercise_10 import uniq_
    f = []
    number_of_plays = 0
    while number_of_plays != 2:
        number_of_plays += 1 
        f.append(Guess_the_number())
    
        print(f)
    
    print(uniq_(f))

uniqPlays()