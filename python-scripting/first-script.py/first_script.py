def check_movie_release(movie, release_year):
    if release_year < 2000:
        print(f"{movie} was released before 2000")
    else:
        print(f"{movie} was released after 2000")
        return movie

recent_movies = []

favorite_movies = [
    ("The Dark Knight", 2008),
    ("Inception", 2010),
    ("Interstellar", 2014),
    ("Fantastic Mr. Fox", 2009),
    ("The Secret Life of Walter Mitty", 2013),
    ("Ferris Bueller's Day Off", 1986),
    ("Forrest Gump", 1994),
    ("The Princess Bride", 1987),
    ("Silence of the Lambs", 1991)
]

for movie, year in favorite_movies:
    result = check_movie_release(movie, year)
    if result is not None:
        recent_movies.append(result)

print("Recent movies:", recent_movies)