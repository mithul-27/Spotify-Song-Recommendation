# Spotify-Song-Recommendation

## Project Overview
This project implements a Music Recommendation System using the Spotify API and Python. It offers two recommendation approaches:
- Content-based Filtering: Recommends songs similar to a user's chosen song based on audio features (danceability, energy, key, etc.).
- Hybrid Approach: Combines content-based filtering with weighted popularity, prioritizing recently released songs with similar audio features.

## Libraries
- mysql-connector-python
- pandas
- numpy
- sklearn
- spotipy
- datetime

## Features
The music recommendation system project outlined in the previous response provides the following features:

### Data Collection and Preprocessing:

- Spotify API Integration: Collects music data from Spotify playlists using the Spotify API.
- Data Extraction: Extracts relevant information from the collected data, such as track name, artists, album name, release date, and audio features.
- Data Cleaning and Preparation: Cleans and prepares the extracted data for analysis and recommendation generation.
- - Data Warehousing: Prepared songs data are pushed to MySQL database using MySQL-python connector.

### Recommendation Algorithms:

- Content-Based Filtering: Recommends songs similar to a user's chosen song based on audio features (danceability, energy, key, etc.).
- Hybrid Approach: Combines content-based filtering with weighted popularity, prioritizing recently released songs with similar audio features.

### Recommendation Generation:

- Similarity Calculation: Calculates similarity scores between songs based on their audio features using cosine similarity.
- Recommendation Selection: Identifies the most similar songs to the user's chosen song based on the calculated similarity scores.
- Recommendation Output: Provides a list of recommended songs with their relevant information, such as track name, artists, album name, release date, and popularity.

### Additional Features:

- Weighted Popularity: Prioritizes recently released songs by assigning higher weights to their popularity scores.
- Hybrid Approach: Combines content-based filtering and weighted popularity for more personalized recommendations.
- User Interaction: Allows users to input song names to receive recommendations.

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
