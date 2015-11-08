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

class ShelTree(nltk.Tree):
    def __init__(self, node, children,parent=None):
        if parent is not None:
            self.parent = parent
        def bla(x):
            if isinstance(x,list):
                return ShelTree(x[0],x[1:],self)
            else:
                return x
        children = filter(bla,children) 
        super(ShelTree,self).__init__(node,children)
        for child in self:
            print(child)
            if not isinstance(child,basestring):
                child.parent = self
    def sub_leaves(self):
        if isinstance(self[0],basestring):
            return [self]
        else:
            leaves = []
            for child in self:
                leaves.extend(child.sub_leaves)
            return leaves
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

#def tree_to_shel(tree):
"""
def tree_to_bare(tree):
    a = [tree.label()]
    for e in tree:
        if isinstance(e,nltk.Tree):
            a.append(tree_to_bare)"""

def shel_tree(t):
    return ShelTree(*t)
    #ShelTree(t[0], [c if isinstance(c, basestring) else shel_tree(c) for c in t[1:]])

def respond(input_str):
    t = parser.raw_parse(input_str)
    input_tr = shel_tree(t)
    print(input_tr)
    return find_similar(input_tr)
    #TODO find similar grammar types as well as exact same grammar type

def debug_ex(c,*glob):
    print(glob)
    c.execute(*glob)
    
def find_similar(tree):
    c = db.conn.cursor()
    goal = 20
    results = []
    shel_stack = tree.sub_leaves()
    while shel_stack and len(results) < goal:
        item  = shel_stack.pop()
        indx = 1
        forms = ["FROM nodes n1 ",""]
        wheres= [" WHERE n1.type=? AND n1.word=?",""]
        paramss = [[ item.label(),item[0] ],[]]
        ancestry = [item]
        count = 1
        combinesql = lambda: (' '.join(forms))+(' '.join(wheres))
        debug_ex(c,"SELECT COUNT(*) "+combinesql(),
                  flatten(paramss))
        count = c.fetchone()[0]
        indx += 1
        while count:
            forms.append(" JOIN nodes n"+str(indx)+" ON n"+str(indx-1)+".parent_id=n"+str(indx)+".id ")
            wheres.append(" AND n%d.type=?" % indx)
            paramss.append(ancestry[-1].label())
            ancestry.append(ancestry[-1].parent)
            debug_ex(c,"SELECT COUNT(*) "+combinesql(),
                      flatten(paramss))
            count = c.fetchone()[0]
            indx += 1
        forms.pop()
        wheres.pop()
        paramss.pop()
        ancestry.pop()
        indx -= 1
        debug_ex(c,"SELECT n"+str(indx)+".rowid "+combinesql(),
                  flatten(paramss))
        for row in c:
            results.append(row[0])
        shel_stack = filter(lambda x: x.has_ancestor(ancestry[-1]),
                            shel_stack)
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
