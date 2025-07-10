import streamlit as st
import pandas as pd
import pickle

# Load data
movies = pd.read_csv('movies.csv')
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie recommendation function
def recommend(movie):
    movie = movie.lower()
    matches = movies[movies['title'].str.lower() == movie]
    if matches.empty:
        return []
    idx = matches.index[0]
    distances = list(enumerate(similarity[idx]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)[1:]  # exclude the movie itself
    return [movies.iloc[i[0]].title for i in distances]

# App title
st.title("🎬 Movie Recommendation System")

# Get movie name from user
movie = st.text_input("Enter a movie name")

# Initialize session state for pagination
if 'num_recs' not in st.session_state:
    st.session_state.num_recs = 5

# Recommend button
if st.button("Recommend"):
    st.session_state.recs = recommend(movie)
    st.session_state.num_recs = 5  # reset when new movie is entered

# Show recommendations
if 'recs' in st.session_state and st.session_state.recs:
    st.subheader(f"Top {st.session_state.num_recs} recommendations:")
    for r in st.session_state.recs[:st.session_state.num_recs]:
        st.write("➡️", r)

    # Show More button
    if st.session_state.num_recs < len(st.session_state.recs):
        if st.button("Show More"):
            st.session_state.num_recs += 5
