import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    df = pd.read_csv("movie.csv")
except FileNotFoundError:
    messagebox.showerror("Error", "movie.csv file not found!")
    exit()

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Genre"])

similarity_matrix = cosine_similarity(tfidf_matrix)

def recommend_movies():

    movie_name = movie_entry.get().strip().lower()

    movie_list = df["Movie"].str.lower().tolist()

    if movie_name not in movie_list:
        messagebox.showerror(
            "Movie Not Found",
            "Please enter a movie from the available list."
        )
        return

    movie_index = df[
        df["Movie"].str.lower() == movie_name
    ].index[0]

    similarity_scores = list(
        enumerate(similarity_matrix[movie_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    result_box.delete("1.0", tk.END)
 
    result_box.insert(
        tk.END,
        f"Selected Movie : {df.iloc[movie_index]['Movie']}\n"
    )

    result_box.insert(
        tk.END,
        f"Genre          : {df.iloc[movie_index]['Genre']}\n"
    )

    result_box.insert(
        tk.END,
        "\nTop 5 Recommended Movies:\n"
    )

    result_box.insert(
        tk.END,
        "-" * 50 + "\n"
    )

    count = 0

    for index, score in similarity_scores:

        if index != movie_index:

            result_box.insert(
                tk.END,
                f"{count + 1}. {df.iloc[index]['Movie']}\n"
                f"   Genre      : {df.iloc[index]['Genre']}\n"
                f"   Similarity : {score * 100:.2f}%\n\n"
            )

            count += 1

        if count == 5:
            break

def clear_all():
    movie_entry.delete(0, tk.END)
    result_box.delete("1.0", tk.END)

def select_movie(event):
    selected = movie_listbox.get(movie_listbox.curselection())
    movie_entry.delete(0, tk.END)
    movie_entry.insert(0, selected)

root = tk.Tk()
root.title("AI Movie Recommendation System")
root.geometry("700x650")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="AI MOVIE RECOMMENDATION SYSTEM",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

movies_label = tk.Label(
    root,
    text="Available Movies",
    font=("Arial", 12, "bold")
)
movies_label.pack()

movie_listbox = tk.Listbox(
    root,
    width=40,
    height=10,
    font=("Arial", 10)
)

for movie in df["Movie"]:
    movie_listbox.insert(tk.END, movie)

movie_listbox.pack(pady=10)

movie_listbox.bind("<<ListboxSelect>>", select_movie)

input_label = tk.Label(
    root,
    text="Enter or Select a Movie",
    font=("Arial", 12)
)
input_label.pack()

movie_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)
movie_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

recommend_button = tk.Button(
    button_frame,
    text="Recommend",
    width=15,
    font=("Arial", 10, "bold"),
    command=recommend_movies
)
recommend_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=15,
    font=("Arial", 10, "bold"),
    command=clear_all
)
clear_button.grid(row=0, column=1, padx=10)


result_label = tk.Label(
    root,
    text="Recommendation Results",
    font=("Arial", 12, "bold")
)
result_label.pack(pady=10)

result_box = tk.Text(
    root,
    width=75,
    height=15,
    font=("Courier New", 10)
)
result_box.pack(pady=10)

note_label = tk.Label(
    root,
    text="Note: This recommendation system features movies from five Indian film industries:\nKannada, Telugu, Tamil, Malayalam, and Hindi.",
    font=("Arial", 9, "italic")
)
note_label.pack(pady=5)

method_label = tk.Label(
    root,
    text="Recommendation Method: TF-IDF Vectorization + Cosine Similarity",
    font=("Arial", 9, "italic")
)
method_label.pack()

total_movies_label = tk.Label(
    root,
    text=f"Total Movies Available: {len(df)}",
    font=("Arial", 10, "bold")
)
total_movies_label.pack(pady=2)

root.mainloop()
