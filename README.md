# Spotify-Song-Recommendation

## Project Overview

This project implements a content-based recommendation system for songs using various music features such as danceability, energy, and tempo. The system suggests songs that are similar to a given input song based on these musical attributes. The recommendations are generated using cosine similarity between normalized feature vectors.

## Features
- Content-Based Recommendations: Generates song recommendations based on song attributes (e.g., tempo, danceability).
- Weighted Popularity Score: Calculates popularity with a weight based on the song’s release date, giving more recent songs a higher score.
- Feature Normalization: Music features are normalized using Min-Max scaling to ensure uniformity in the recommendation calculations.

## Project Structure
- Spotify_Recomendation.ipynb: This Jupyter Notebook contains the entire implementation of the recommendation system, including the following steps:
- Data Loading: Load the dataset of songs with their attributes.
- Feature Normalization: Normalize the relevant song features (danceability, energy, tempo, etc.) using Min-Max scaling.
- Weighted Popularity Calculation: A custom function computes the popularity weight of songs based on how recently they were released.
- Content-Based Filtering: A recommendation function computes cosine similarity between the input song’s features and all other songs in the dataset, then suggests the top similar songs.  

- app.py: This py file contains the streamlit app part to display the recommendations based on the user input
- User has to type the name of the song to get recommendation based on the song
- If the song entered is in the database, recommended songs are shown. Else it displays that the songs entered is not found.
- Based on the song entered, top 10 recommendations are displayed.
![image](https://github.com/user-attachments/assets/541b6086-ceea-4b03-a59b-18375eab42b4)
