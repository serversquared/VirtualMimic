from parser import parser
import nltk
import db
"""this is absolutely pointless
class Node():
    def __init__(self,id,parent,type,order,word):
        self.id    = id
        self.parent= parent
        self.type  = type
        self.order = order
        self.word  = word
        self.children = []
        c = db.conn.cursor()
        c.execute("SELECT * FROM nodes WHERE parent_id=?",(id))
        for row in c.fetchmany:
            self.children.append(Node(*row))
        c.close()
"""
#db.conn.cursor()
#    resu

class nltk.Tree:
    def sub_leaves(self):
        if isinstance(self[0],str):
            return [self]
        else:
            leaves = []
            for child in self:
                leaves.extend(child.sub_leaves)
            return leaves

def respond(input_str):
    input = parser.parse(input_str)
    #TODO find similar grammar types as well as exact same grammar type

def find_similar(tree):
    c = db.conn.cursor()
    stuff = {}
    goal = 20
    results = []
    stack = tree.sub_leaves
    for
    while stack:
        item = stack.pop!
        statements = ["FROM nodes n1 WHERE type=? AND word=?"]
        paramss = [[ item.label(),item[0] ]]
        count = 1
        while count:
            c.execute("SELECT COUNT(*) "+statements[-1],paramss[-1])
            count = c.fetchone()[0]
            


"""
def depth_search(c,node,results,num_results):
    if type(node[0]) == nltk.Tree:
        for child in node:
            res = depth_search(c,child,results,num_results)
            break if res
        if res:
            
    else: #this is a ending node
        c.execute("SELECT COUNT(*) FROM nodes WHERE type=?,word=?",
                  (node.label(),node[0]))
        count = c.fetchone()[0]
        return count




        '''
        if results.length + count > num_results:
            #wooo, were done
            c.execute("""SELECT * FROM nodes WHERE type=?,word=?
                      LIMIT ?""",
                      (node.label(), node[0], num_results - results.length))
            return true
        else:
            c.execute("""SELECT * FROM nodes WHERE type=?,word=?""",
                      (node.label(),node[0]))
            return c.findall()'''
