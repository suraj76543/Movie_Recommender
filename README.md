## End to End Movie Recommendation Project using TMDB rating
# Movie Recommender System using Machine Learning

This **Movie Recommender System** is a content-based recommendation engine that helps users discover movies similar to their interests. The system uses natural language processing (NLP) and machine learning techniques to suggest films based on a given movie's metadata, such as genre, cast, and crew and Tags.

## Features

- Recommends 5 similar movies based on user input.
- Built using **Python**, **Machine Learning**, and **NLP** techniques.
- Uses **cosine similarity** to calculate movie similarity based on metadata.
- Deployed with **Streamlit** for an interactive web interface.

## Technologies

- **Python**
- **Pandas**
- **Scikit-learn** (for machine learning)
- **Natural Language Processing (NLP)**
- **Streamlit** (for web deployment)
- **CountVectorizer** (for text vectorization)
- **Cosine Similarity** (for finding similar movies)

## Project Structure
Movie_Recommender
│
├── app.py
├── movies.csv
├── similarity_matrix.pkl
├── requirements.txt
└── README.md

How it Works
Preprocessing: Data cleaning and handling missing values.

Feature Engineering: Merging columns to create textual features (e.g., genre, overview, keywords).

NLP Techniques: Tokenization and stemming applied to text data.

Vectorization: Using CountVectorizer to convert text into numerical data.

Similarity Calculation: Cosine similarity is used to find the top 5 similar movies.

## Project Description 
The movie recommender system effectively generates relevant movie suggestions based on user input by analyzing key textual features like genres, cast, crew, and plot summaries. Using a content-based approach, the system doesn't rely on user ratings or history, making it suitable for new users or those with minimal interaction data. It delivers real-time recommendations through a simple web interface, ensuring a seamless user experience. User feedback confirms that the system aligns well with the thematic and stylistic preferences of the input movie, indicating that the recommendations are accurate.


