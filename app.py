import streamlit as st
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import datetime
from sklearn.metrics.pairwise import cosine_similarity
import mysql.connector


icon='https://avatars.githubusercontent.com/u/251374?v=4'
st.set_page_config(page_title='Spotify Song Recommendation',page_icon=icon,initial_sidebar_state='expanded',
                        layout='wide')

title_text = '''<h1 style='font-size: 36px;color:#85D265;text-align: center;'>Spotify Song Recommendation</h1><h2 style='font-size: 24px;color:#61A446;text-align: center;'>Get Song Recommendation from your choice</h2>'''
st.markdown(title_text, unsafe_allow_html=True)

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["database"]["host"],
        user=st.secrets["database"]["user"],
        password=st.secrets["database"]["password"],
        database=st.secrets["database"]["database"],
        port=int(st.secrets["database"]["port"])
    )
conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM Tamil_songs")
result = cursor.fetchall()
songs_df = pd.DataFrame(result, columns=[i[0] for i in cursor.description])

# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='YOUR_CLIENT_ID',
                                                           client_secret='YOUR_CLIENT_SECRET'))



def calculate_weighted_popularity(release_date):
   
    # Calculate the time span between release date and today's date
    time_span = datetime.datetime.strptime("2024-09-14", '%Y-%m-%d') - release_date

    # Calculate the weighted popularity score based on time span (e.g., more recent releases have higher weight)
    weight = 1 / (time_span.days + 1)
    return weight

# Normalize the music features using Min-Max scaling
scaler = MinMaxScaler()
music_features = songs_df[['Danceability', 'Energy', 'Key_note',
                           'Loudness', 'Mode', 'Speechiness', 'Acousticness',
                           'Instrumentalness', 'Liveness', 'Valence', 'Tempo']].values
music_features_scaled = scaler.fit_transform(music_features)

# a function to get content-based recommendations based on music features
def content_based_recommendations(input_song_name, num_recommendations=10):
    if input_song_name not in songs_df['Track_Name'].values:
        print(f"'{input_song_name}' not found in the dataset. Please enter a valid song name.")
        return

    # Get the index of the input song in the music DataFrame
    input_song_index = songs_df[songs_df['Track_Name'] == input_song_name].index[0]

    # Calculate the similarity scores based on music features (cosine similarity)
    similarity_scores = cosine_similarity([music_features_scaled[input_song_index]], music_features_scaled)

    # Get the indices of the most similar songs
    similar_song_indices = similarity_scores.argsort()[0][::-1][1:num_recommendations + 1]

    # Get the names of the most similar songs based on content-based filtering
    content_based_recommendations = songs_df.iloc[similar_song_indices][['Track_Name', 'Artists', 'Album_Name', 'Release_Date', 'Popularity']]

    return content_based_recommendations

def hybrid_recommendations(input_song_name, num_recommendations=10, alpha=0.5):
    if input_song_name not in songs_df['Track_Name'].values:
        print(f"'{input_song_name}' not found in the dataset. Please enter a valid song name.")
        return

    content_based_rec = content_based_recommendations(input_song_name, num_recommendations)

    popularity_score = songs_df.loc[songs_df['Track_Name'] == input_song_name, 'Popularity'].values[0]

    weighted_popularity_score = popularity_score * calculate_weighted_popularity(
        songs_df.loc[songs_df['Track_Name'] == input_song_name, 'Release_Date'].values[0]
    )

    new_entry = pd.DataFrame({
        'Track_Name': [input_song_name],
        'Artists': [songs_df.loc[songs_df['Track_Name'] == input_song_name, 'Artists'].values[0]],
        'Album_Name': [songs_df.loc[songs_df['Track_Name'] == input_song_name, 'Album_Name'].values[0]],
        'Release_Date': [songs_df.loc[songs_df['Track_Name'] == input_song_name, 'Release_Date'].values[0]],
        'Popularity': [weighted_popularity_score]
    })

    hybrid_recommendations = pd.concat([content_based_rec, new_entry], ignore_index=True)

    hybrid_recommendations = hybrid_recommendations.sort_values(by='Popularity', ascending=False)

    hybrid_recommendations = hybrid_recommendations[hybrid_recommendations['Track_Name'] != input_song_name]

    return hybrid_recommendations

st.markdown("### :red[Available Songs:] Popular Tamil songs")
# Input for the song name to get recommendations
query = st.text_input('Enter a song name to get recommendations:')

if query:
    # Find the track in the CSV file
    track = songs_df[songs_df['Track_Name'].str.contains(query, case=False, na=False)]
    if not track.empty:
        track_name = track.iloc[0]['Track_Name']
        st.write(f"Track found: {track.iloc[0]['Track_Name']} by {track.iloc[0]['Artists']}")
        
        # Get recommendations based on the track ID
        recommendations_df = hybrid_recommendations(track_name,num_recommendations=10)
        
        # Display recommendations
        st.subheader('Recommended Songs:')
        st.dataframe(recommendations_df.style.set_properties(**{
                    'background-color': 'lightblue',
                    'color': 'black',
                    'border-color': 'white'
                }))

    else:
        st.write("No matching tracks found. Try a different query.")
