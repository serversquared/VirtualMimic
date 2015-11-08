import stat_parser
import nltk
import db

parser = Parser()

def insert_node(cursor,type,order=0,parent_id=None,word=None):
    cursor.execute("INSERT INTO nodes (parent_id,type,order,word) VALUES ?,?,?,?"
                   ,(parent_id,type,order,word))

def insert_tree(cursor,node,order=1,parent_id=None):
    if type(node) == nltk.Tree:
        insert_node(cursor,node[0],order,parent_id)
        parent_id = cursor.lastrowid
        for i,child in enumerate(node[1:]):
            insert_tree(cursor,child,i,parent_id)
        cursor.execute("COMMIT")
    else:
        insert_node(cursor,"WORD",order,parent_id)
    return parent_id

def insert_struct(sentence,weight=1):
    global parser
    cursor = db.conn.cursor()
    return insert_tree(cursor,parser.parse(sentence))

def feed(input, response, weight):
    input_id = insert_struct(input)
    response_id = insert_struct(response)
    db.conn.execute("INSERT INTO nodes_to_nodes VALUES ?,?,?",input_id, response_id)
