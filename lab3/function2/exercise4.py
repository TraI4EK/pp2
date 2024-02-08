from movie import movies
def average_imdb_score(movies : list):
    score_overall = 0
    for movie in movies:
        score_overall += movie["imdb"]

    return score_overall / len(movies)


print(average_imdb_score(movies))