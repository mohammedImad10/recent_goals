import sqlite3

print("asdasdasdasdasd")
connection = sqlite3.connect("db.sqlite3") 
cursor = connection.cursor()

# Query to get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the table names
print("Tables in the database:")
for table in tables:
    print(table[0])

cursor.execute("SELECT * FROM score_bat_highlights_bathighlight;")
tables = cursor.fetchall()

print("!" * 40)
for table in tables:
    print(table[0])
cursor.execute("PRAGMA table_info(score_bat_highlights_bathighlight);")
columns = cursor.fetchall()
cursor.execute("DELETE FROM django_migrations WHERE app='your-app-name';")

# Print the columns
for column in columns:
    print(column)
# Close the connection
connection.close()

