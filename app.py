import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os
import gdown  # For downloading from Google Drive

# === Auto-download .pkl files if missing ===
if not os.path.exists('movie_dict.pkl'):
    url = 'https://drive.google.com/file/d/1AoTHHhAiQBpwxZs_jxfyAtx_tinfo_Z2/view?usp=sharing'
    gdown.download(url, 'movie_dict.pkl', quiet=False, fuzzy=True)

if not os.path.exists('similarity.pkl'):
    url = 'https://drive.google.com/file/d/1AlIll-afaTudLQ5BsNr6Pmvwh3NUy0XG/view?usp=drive_link'
    gdown.download(url, 'similarity.pkl', quiet=False, fuzzy=True)

# === Load the pickle files ===
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# === Recommendation function ===
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# === Streamlit App Frontend ===
st.title("Personalized Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Which type of movie would you like to watch?",
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
