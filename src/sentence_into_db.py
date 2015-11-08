import stat_parser
import nltk
import db

parser = stat_parser.Parser()

def insert_node(cursor,gtype,order=0,parent_id=None,word=None):
    #print(type(gtype))
    #print(gtype)
    cursor.execute("""INSERT INTO nodes (`parent_id`,`type`,`order`,`word`)
                   VALUES (?,?,?,?)""",
                   (parent_id,gtype,order,word))


def insert_tree(cursor,node,order=1,parent_id=None):
    if type(node) == nltk.Tree:
        insert_node(cursor,node.label(),order,parent_id)
        parent_id = cursor.lastrowid
        for i,child in enumerate(node):
            insert_tree(cursor,child,i,parent_id)
        #cursor.execute("COMMIT")
    else:
        insert_node(cursor,"WORD",order,parent_id, node)
    return parent_id

def insert_struct(sentence,weight=1):
    global parser
    cursor = db.conn.cursor()
    res = insert_tree(cursor,parser.parse(sentence))
    db.conn.commit()
    cursor.close()
    return res

def feed(input, response, weight=1):
    input_id = insert_struct(input)
    response_id = insert_struct(response)
    db.conn.execute("INSERT INTO nodes_to_nodes VALUES (?,?,?)",
                    (input_id, response_id, weight))
