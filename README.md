## End to End Movie Recommendation Project using TMDB rating
# Movie Recommender System using Machine Learning

This **Movie Recommender System** is a content-based recommendation engine that helps users discover movies similar to their interests. The system uses natural language processing (NLP) and machine learning techniques to suggest films based on a given movie's metadata, such as genre, cast, and crew and Tags.

## 🚀 Features

- Recommends 5 similar movies based on user input.
- Built using **Python**, **Machine Learning**, and **NLP** techniques.
- Uses **cosine similarity** to calculate movie similarity based on metadata.
- Deployed with **Streamlit** for an interactive web interface.

## 📊 Technologies

- **Python**
- **Pandas**
- **Scikit-learn** (for machine learning)
- **Natural Language Processing (NLP)**
- **Streamlit** (for web deployment)
- **CountVectorizer** (for text vectorization)
- **Cosine Similarity** (for finding similar movies)

## 📂 Project Structure
Movie_Recommender/
│
├── app.py # Streamlit web application
├── movies.csv # Dataset containing movie metadata
├── similarity_matrix.pkl# Precomputed movie similarity matrix
├── requirements.txt # Required Python packages
└── README.md # Project documentation

How it Works
Preprocessing: Data cleaning and handling missing values.

Feature Engineering: Merging columns to create textual features (e.g., genre, overview, keywords).

NLP Techniques: Tokenization and stemming applied to text data.

Vectorization: Using CountVectorizer to convert text into numerical data.

Similarity Calculation: Cosine similarity is used to find the top 5 similar movies.
