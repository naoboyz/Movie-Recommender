import pandas as pd

def load_data():
    movies = pd.read_csv("u.item", sep="|", encoding="latin-1", header=None, usecols=[0, 1], names=["movie_id", "title"])
    ratings = pd.read_csv("u.data", sep="\t", names=["user_id", "movie_id", "rating", "timestamp"])
    return movies, ratings
