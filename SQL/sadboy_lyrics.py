import sqlite3

# Connect to the database
conn = sqlite3.connect("sadboy_lyrics.db")
cursor = conn.cursor()

# Check if the artist_image_url column exists and add it if not
cursor.execute("PRAGMA table_info(songs)")
columns = [column[1] for column in cursor.fetchall()]
if "artist_image_url" not in columns:
    cursor.execute("ALTER TABLE songs ADD COLUMN artist_image_url TEXT")

# Prompt the user to enter the lyrics but everything else is filled in
song_name = "On My Ones"
artist = "MoStack"
lyrics = input("Enter the lyrics: ")

# Insert a row into the table
cursor.execute("INSERT INTO songs (song_name, artist, lyrics) VALUES (?, ?, ?)", (song_name, artist, lyrics))
song_id = cursor.lastrowid

# Check if there is an existing image URL for the artist
cursor.execute("SELECT artist_image_url FROM songs WHERE artist=? AND artist_image_url IS NOT NULL AND artist_image_url != '' LIMIT 1", (artist,))
result = cursor.fetchone()

if result:
    # An image URL exists, update the new record with it
    artist_image_url = result[0]
    cursor.execute("UPDATE songs SET artist_image_url=? WHERE song_id=?", (artist_image_url, song_id))
else:
    # No image URL exists, prompt for one
    artist_image_url = input(f"Enter the image URL for the artist {artist}: ")
    cursor.execute("UPDATE songs SET artist_image_url=? WHERE song_id=?", (artist_image_url, song_id))

# Save the changes to the database
conn.commit()

# Close the database connection
conn.close()
