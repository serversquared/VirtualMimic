import sqlite3

conn = sqlite3.connect("main.db")
cursor = conn.cursor()
f = open("schema.sql")
cursor.executescript(f.read())
