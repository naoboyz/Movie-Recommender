from load_data import load_data
from recommender import build_content_model, recommend_movies
from sentiment import get_sentiment

movies, ratings = load_data()
similarity_matrix = build_content_model(movies)

print(" Welcome to Smart Movie Recommender 🎬")
fav_movie = input("Enter a movie you like: ")
mood_text = input("How are you feeling today? ")

sentiment = get_sentiment(mood_text)
print(f"\n Detected mood: {sentiment}\n")

recs = recommend_movies(fav_movie, movies, similarity_matrix)

if sentiment == "positive":
    print("You're in a good mood! You might enjoy these uplifting movies:")
elif sentiment == "negative":
    print("Feeling down? These might cheer you up:")
else:
    print("Here are some similar movies you might like:")

for movie in recs:
    print(" -", movie)
