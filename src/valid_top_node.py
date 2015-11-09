import db

def valid_top_node(i, c=db.conn.cursor()):
    c.execute("SELECT COUNT(*) FROM nodes_to_nodes WHERE input=?",(i,))
    count = c.fetchone()[0]
    return (count > 0)
