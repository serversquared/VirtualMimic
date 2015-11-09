import db

c = db.conn.cursor()
c.execute("SELECT rowid,parent_id,word FROM nodes WHERE word NOT NULL")
for row in c.fetchall():
	c.execute("UPDATE nodes SET word=? WHERE rowid=?",(row[2],row[1]))
c.execute("SELECT rowid FROM nodes WHERE is_response=1 AND parent_id IS NULL")
stack = c.fetchall()
i = 0
while len(stack) > 0:
        row = stack.pop()
        c.execute("UPDATE nodes SET is_response=1 WHERE parent_id=?",(row[0],))
        c.execute("SELECT rowid FROM nodes WHERE parent_id=?",(row[0],))
        stack += c.fetchall()
        i += 1
        if i % 100 == 0:
                db.conn.commit()
        if i % 1000== 0:
                print("on iter %d, stack size is %d" % (i,len(stack)))
        
db.conn.commit()
