import sqlite3
 
# connecting to the database
connection = sqlite3.connect(r"C:\discordbot\SQL\brilliant_count.db")
# or connection = sqlite3.connect("brilliant_count.db")

# cursor
crsr = connection.cursor()
 
# # SQL command to create a table in the database
# sql_command = """CREATE TABLE brilliant_counter (
# discord_username VARCHAR(30),
# discord_id VARCHAR(30),
# count INT);"""
# crsr.execute(sql_command)
# # SQL command to insert the data in the table
# sql_command = """INSERT INTO brilliant_counter VALUES ("vistoso",1);"""
# crsr.execute(sql_command)

# rows = crsr.execute("SELECT discord_username, brilliant_count FROM brilliant_count").fetchall()
# print(rows) 

# sql_command = """UPDATE brilliant_count SET brilliant_count = brilliant_count + 1 WHERE discord_username = 'pele'"""
# crsr.execute(sql_command)

crsr.execute("SELECT * FROM brilliant_counter")
crsr.execute("DELETE FROM brilliant_counter")

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit() 
# close the connection
connection.close()