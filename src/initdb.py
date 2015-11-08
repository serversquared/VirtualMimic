import sqlite3

def initDb():
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    f = open("schema.sql")
    cursor.executescript(f.read())
