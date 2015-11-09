import sqlite3
import os.path
from yoyo import read_migrations
import yoyo.connections 

import initdb

if not os.path.isfile("main.db"):
    initdb.initDb()

conn = sqlite3.connect("main.db")
"""
migrations = read_migrations(conn, 'qmark', "migrations")
if len(migrations.to_apply()) > 0:
    sys.argv.write("WARN: Migrations are pending")"""
