import sqlite3

# Connect to the database
conn = sqlite3.connect("sadboy_lyrics.db")
cursor = conn.cursor()

# Add the artist_image_url column to the table
cursor.execute("ALTER TABLE songs ADD COLUMN artist_image_url TEXT")

# Select all rows from the table
cursor.execute("SELECT * FROM songs")
rows = cursor.fetchall()

# Create a set to store the unique artists
artists = set()

# Loop through the rows and add each artist to the set (row [2] is artist column)
for row in rows:
    artists.add(row[2])

# Loop through the unique artists
for artist in artists:
    # Prompt the user to enter the image URL
    artist_image_url = input(f"Enter the image URL for the artist {artist}: ")

    # Update the rows in the table for the artist
    cursor.execute("UPDATE songs SET artist_image_url=? WHERE artist=?", (artist_image_url, artist))

# Save the changes to the database
conn.commit()

# Close the database connection
conn.close()