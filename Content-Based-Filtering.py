# Data film dengan atribut genre
movies = {
    'Movie1': ['Action', 'Adventure', 'Sci-Fi'],
    'Movie2': ['Drama', 'Romance'],
    'Movie3': ['Action', 'Adventure'],
    'Movie4': ['Comedy', 'Romance'],
    'Movie5': ['Action', 'Comedy', 'Drama'],
}

# Fungsi untuk merekomendasikan film berdasarkan genre


def recommend_movies(user_genre, movies):
    recommended_movies = []

    for movie, genres in movies.items():
        # Hitung overlap antara genre yang dimiliki oleh pengguna dan genre film
        genre_overlap = set(user_genre).intersection(genres)

        # Hitung skor berdasarkan jumlah genre yang sama
        score = len(genre_overlap)

        # Filter film-film yang memiliki minimal satu genre yang sama
        if score > 0:
            recommended_movies.append((movie, score))

    # Sort rekomendasi berdasarkan skor tertinggi
    recommended_movies.sort(key=lambda x: x[1], reverse=True)

    return recommended_movies


# Genre yang disukai oleh pengguna
user_favorite_genre = ['Action', 'Adventure']

# Merekomendasikan film berdasarkan genre yang disukai oleh pengguna
recommendations = recommend_movies(user_favorite_genre, movies)

# Cetak film-film yang direkomendasikan
print("Film-film yang direkomendasikan:")
for movie, score in recommendations:
    print(f"{movie} (Skor: {score})")
