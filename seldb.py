import sqlite3
import sel

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()
sql = "SELECT * FROM movies"
cursor.execute(sql)

if cursor.fetchall() != sel.result:
    cursor.execute("DELETE FROM movies")
    cursor.executemany("INSERT INTO movies VALUES (?,?,?)", sel.result)
    conn.commit()

conn.close()