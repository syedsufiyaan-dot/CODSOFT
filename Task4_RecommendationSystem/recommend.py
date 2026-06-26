import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("movies.csv")

tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(data['genre'])

similarity = cosine_similarity(matrix)

def recommend(movie):
    if movie not in data['title'].values:
        print("Movie not found!")
        return

    index = data[data['title'] == movie].index[0]
    distances = list(enumerate(similarity[index]))

    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    print("\nRecommended movies:\n")

    for i in sorted_movies:
        print(data.iloc[i[0]].title)

recommend("Inception")
