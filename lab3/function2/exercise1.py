from movie import movies
def is_movie_imdb_above(movie : str):
    for m in movies:
        if m["name"] == movie:
            return m["imdb"] > 5.5
    
    return False


print(is_movie_imdb_above("The Help"))