from parser import parser
from array_flatten import flatten
import nltk
from nltk import Tree
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

class Tree():
    def sub_leaves(self):
        if isinstance(self[0],str):
            return [self]
        else:
            leaves = []
            for child in self:
                leaves.extend(child.sub_leaves)
            return leaves

class ShelTree(nltk.Tree):
    def __init__(self, node, children,parent=None):
        if parent is not None:
            self.parent = parent
        super(self,node,children)
        for child in self:
            child.parent = self
    def siblings(self):
        if self.parent is None: return []
        return self.parent.children
    def has_ancestor(self,ancestor,by_id = False):
        p = self.parent
        while p is not None:
            if by_id and id(p) == id(ancestor):
                return True 
            elif p == ancestor:
                return True
        return False

def respond(input_str):
    input = parser.parse(input_str)
    #TODO find similar grammar types as well as exact same grammar type

def find_similar(tree):
    c = db.conn.cursor()
    goal = 20
    results = []
    stack = tree.sub_leaves
    while stack and len(results) < goal:
        item  = stack.pop()
        indx = 1
        froms = ["FROM nodes n1"]
        wheres= ["WHERE n1.type=? AND n1.word=?"]
        paramss = [[ item.label(),item[0] ]]
        ancestry = [item]
        count = 1
        combinesql = lambda: (' '.join(forms))+(' '.join(wheres))
        c.execute("SELECT COUNT(*) "+combinesql(),
                  flatten(paramss))
        count = c.fetchone()[0]
        indx += 1
        while count:
            forms.append("JOIN nodes n"+str(indx)+" ON n"+str(indx-1)+".parent_id=n"+str(indx)+".id ")
            wheres.append(" AND n%d.type=?" % indx)
            paramss.append(ancestry[-1].label())
            ancestry.append(ancestry[-1].parent)
            c.execute("SELECT COUNT(*) "+combinesql(),
                      flatten(paramss))
            count = c.fetchone()[0]
            indx += 1
        froms.pop()
        wheres.pop()
        paramss.pop()
        ancestry.pop()
        c.execute("SELECT n"+int(indx)+".rowid "+combinesql(),
                  flatten(paramss))
        for row in c:
            results.append(row[0])
        stack = filter(lambda x: x.has_ancestor(ancestry[-1]),stack)
    return results

'''
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
