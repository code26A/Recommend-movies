# 🎬 Movie Recommendation System

This is a simple **content-based movie recommender system** built using Python. It recommends similar movies based on the content (genres, cast, director, etc.) of a selected movie.

---

## 💡 How it Works

- Uses **TF-IDF** or **CountVectorizer** to convert movie tags into vectors.
- Calculates **cosine similarity** between vectors.
- Recommends the top N similar movies to the one selected.

---

## 🧠 Tech Stack

- Python
- Pandas
- scikit-learn (TF-IDF / CountVectorizer, cosine_similarity)
- Streamlit (for frontend interface)
- Pickle (to store precomputed similarity matrix)

---

## 🗃 Files Used

| File                         | Description                                      |
|------------------------------|--------------------------------------------------|
| `tmdb_5000_movies.csv`       | Cleaned movie metadata (title, tags, etc.)       |
| `tmdb_5000_credits.csv`      | Cleaned movie metadata (title, tags, etc.)       |
| `app.py`                     | Streamlit app to interact with recommender       |
| `requirements.txt`           | Python dependencies                              |
| `Movie_Recommendation.ipynb` | Jupyter Notebook File                            |

---


