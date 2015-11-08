import db

c = db.conn.cursor()
c.execute("SELECT rowid,parent_id,word FROM nodes WHERE word NOT NULL")
for row in c.fetchall():
	c.execute("UPDATE nodes SET word=? WHERE rowid=?",(row[2],row[1]))
db.conn.commit()
