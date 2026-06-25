# AI Movie Recommender Using Python

## Description
The AI Movie Recommendation System is a Machine Learning-based desktop application developed using Python. It recommends movies to users based on the similarity of movie genres. The system uses TF-IDF (Term Frequency–Inverse Document Frequency) to convert movie genres into numerical vectors and Cosine Similarity to measure the similarity between movies. Users can either select a movie from the available list or type its name, and the application displays the top five most similar movie recommendations along with their genres and similarity percentages. The system includes movies from five major Indian film industries: Kannada, Telugu, Tamil, Malayalam, and Hindi.

## Features

- Recommends the **Top 5 similar movies** based on genre.
- Uses **TF-IDF Vectorization** for text feature extraction.
- Uses **Cosine Similarity** to calculate movie similarity.
- User-friendly GUI built with Tkinter.
- Displays the selected movie and its genre.
- Shows similarity percentage for each recommended movie.
- Includes a searchable movie list.
- Allows users to select movies directly from a Listbox.
- Clear button to reset inputs and results.
- Displays the total number of movies available in the dataset.
- Features movies from **Kannada, Telugu, Tamil, Malayalam, and Hindi** film industries.

## Technologies Used                            
- Python           
- Tkinter          
- Pandas
- Scikit-learn      
- TF-IDF Vectorizer 
- Cosine Similarity              
- CSV Dataset                           

## Project Structure

```
AI-Movie-Recommendation-System/
│── movie.csv
│── Movie_Recommender.py

```

## Dataset
- movie.csv
- This project uses a custom movie dataset containing movies from five major Indian film industries.
  
### Dataset Information
* **Dataset Name:** movie.csv
* **Total Movies:** 50+ 
* **Film Industries:**
  * Kannada
  * Telugu
  * Tamil
  * Malayalam
  * Hindi
* **File Format:** CSV

> **Note:** Save the dataset as **movie.csv** in the project folder before running the application.

##  Installation

###  Install required libraries

```bash
pip install pandas scikit-learn
```

*(Tkinter is included with most Python installations.)*


## Run the Project

```bash
python Movie_Recommender.py
```

##  Working Process

1. Load the **movie.csv** dataset.
2. Read the movie names and genres.
3. Convert movie genres into TF-IDF feature vectors.
4. Calculate similarity using Cosine Similarity.
5. Display the list of available movies.
6. Select or enter a movie name.
7. Click **Recommend**.
8. Display the selected movie, its genre, and the Top 5 recommended movies with similarity scores.


## Sample Output

### Example

**Input**

```
KGF Chapter 1
```

**Output**

```
Selected Movie : KGF Chapter 1
Genre          : Action Drama

Top 5 Recommended Movies

1. KGF Chapter 2
   Genre      : Action Drama
   Similarity : 100.00%

2. Salaar
   Genre      : Action Thriller
   Similarity : 84.25%

3. Vikram
   Genre      : Action Crime
   Similarity : 79.84%

4. Kantara
   Genre      : Action Thriller
   Similarity : 77.61%

5. Pushpa
   Genre      : Action Drama
   Similarity : 74.38%
```



