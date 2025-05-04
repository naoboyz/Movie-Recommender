from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_content_model(movies):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['title'])
    similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return similarity

def recommend_movies(title, movies, similarity_matrix, top_n=5):
    if title not in movies['title'].values:
        return ["Movie not found."]
    idx = movies[movies['title'] == title].index[0]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in scores[1:top_n+1]]
    return movies['title'].iloc[top_indices].tolist()
