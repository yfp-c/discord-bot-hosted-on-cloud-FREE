import sqlite3

# Connect to the database
conn = sqlite3.connect("sadboy_lyrics.db")
cursor = conn.cursor()

# Create the table
# cursor.execute("CREATE TABLE songs (song_id INTEGER PRIMARY KEY, song_name TEXT, artist TEXT, lyrics TEXT)")

# # Prompt the user to enter the song name, artist, and lyrics
# song_name = input("Enter the song name: ")
# artist = input("Enter the artist: ")
# lyrics = input("Enter the lyrics: ")

# Prompt the user to enter the lyrics but everything else is filled in
song_name = "BE MY MELODY"
artist = "Seo In Guk (서인국)"
lyrics = input("Enter the lyrics: ")

# Insert a row into the table
cursor.execute("INSERT INTO songs (song_id, song_name, artist, lyrics) VALUES (NULL, ?, ?, ?)", (song_name, artist, lyrics))

# # Prompt the user to enter the song_id of the row to delete
# song_id = input("Enter the song_id of the row to delete: ")

# # Delete the row from the table
# cursor.execute("DELETE FROM songs WHERE song_id=?", (song_id,))

# Save the changes to the database
conn.commit()

# Close the database connection
conn.close()