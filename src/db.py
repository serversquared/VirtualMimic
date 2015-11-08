import sqlite3
import os.path

if not os.path.isfile("main.db"):
    print("main.db does not exist, please run initdb.py")
    exit(1)

conn = sqlite3.connect("main.db")
