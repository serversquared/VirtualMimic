import produce_response as pr
import db
from valid_top_node import *
c = db.conn.cursor()
res = pr.respond("Hello I would like to inquire as to the expeiriences of what common sentences you may know about in the current time frame")
for i in res:
    if valid_top_node(i):
        print("%d is good!" % i)
    else:
        print("%d is bad" % i)
