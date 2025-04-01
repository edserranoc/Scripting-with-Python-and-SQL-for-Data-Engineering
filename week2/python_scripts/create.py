# import SQLite
import sqlite3

# The next thing that you want to do is create a connection. 
# I'm just going to name it sample.db
connection = sqlite3.connect('sample.db')

# I want to create a table
table = 'CREATE TABLE people (id integer primary key, name TEXT,surname TEXT)'
cursor = connection.cursor()
cursor.execute(table)
connection.commit()