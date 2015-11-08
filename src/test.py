import sentence_into_db as sid
import sqlite3
import db
'''
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE bla (foo int)")
db.execute("INSERT INTO bla (foo) VALUES (?)", (None,))
'''
sid.feed("I am awesome.", "Yes you are.")

db.conn.commit()
db.conn.close()
