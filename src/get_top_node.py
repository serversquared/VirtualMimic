import db

def get_top_node(node_id,cursor=None):
    shouldclose = False
    if cursor is None:
        cursor = db.conn.cursor()
        shouldclose = True
    while True:
        cursor.execute("SELECT parent_id FROM nodes WHERE rowid=?",
                       (node_id,))
        row = cursor.fetchone()
        if row is None:
            raise TypeError("invalid node_id, or node_id is part of invalid tree structure")
        if row[0] is None: #Cave Johnson
            return node_id #We're done here.
        node_id = row[0]
            
