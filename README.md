# AI Movie Recommender Using Python
# Description
The AI Movie Recommendation System is a Machine Learning-based desktop application developed using Python. It recommends movies to users based on the similarity of movie genres. The system uses TF-IDF (Term Frequency–Inverse Document Frequency) to convert movie genres into numerical vectors and Cosine Similarity to measure the similarity between movies. Users can either select a movie from the available list or type its name, and the application displays the top five most similar movie recommendations along with their genres and similarity percentages. The system includes movies from five major Indian film industries: Kannada, Telugu, Tamil, Malayalam, and Hindi.

## Features
- User-friendly GUI developed using Tkinter.
- Displays a list of all available movies.
- Allows users to select or manually enter a movie name.
- Recommends the Top 5 similar movies.
- Uses TF-IDF Vectorization.
- Uses Cosine Similarity.
- Includes Clear button.
- Handles invalid movie names.

## Installation
```bash
pip install pandas scikit-learn
```

## How to Run
```bash
python Movie_Recommender.py
```

## Dataset
- movie.csv

## Technologies Used
- Python
- Tkinter
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
