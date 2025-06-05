import sqlite3

conn = sqlite3.connect("submissions.db")
cursor = conn.cursor()
cursor.execute("SELECT id, timestamp, name FROM submissions ORDER BY id DESC")
rows = cursor.fetchall()
conn.close()

for row in rows:
    print(row)