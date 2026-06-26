# Task 4 - Recommendation System

## 📌 Objective
Build a simple recommendation system that suggests similar movies based on their genres using Content-Based Filtering.

## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

## 📂 Files
- `recommend.py` - Main Python program
- `movies.csv` - Movie dataset
- `README.md` - Project documentation

## 🚀 How to Run

1. Install the required libraries:

```bash
pip install pandas scikit-learn
```

2. Run the program:

```bash
python recommend.py
```

## 📊 Sample Output

```
Recommended movies:

Interstellar
The Dark Knight
Avengers
Doctor Strange
Joker
```

## 📖 How It Works

- Loads the movie dataset.
- Converts movie genres into numerical features using TF-IDF.
- Calculates similarity between movies using Cosine Similarity.
- Recommends the most similar movies based on the selected movie.

## 🎯 Features

- Simple content-based recommendation system.
- Fast and easy to understand.
- Uses machine learning concepts.
- Can be extended with larger datasets.

## 👨‍💻 Author

**Syed Sufiyaan**
