import sqlite3
import os.path

import initdb

if not os.path.isfile("main.db"):
    initdb.initDb()

conn = sqlite3.connect("main.db")
