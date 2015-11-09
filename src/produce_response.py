import nltk
from nltk import Tree

from array_flatten import flatten
from parser import parser
from get_top_node import get_top_node
import db

class ShelTree(nltk.Tree):
    def __init__(self, node, children,parent=None):
        #print('node')
        #print(node)
        #print('children')
        #print(children)
        if parent is not None:
            self._parent = parent
        """
        def bla(x):
            #print(x)
            if isinstance(x,list):
                return ShelTree(x[0],x[1:],self)
            else:
                #print('else')
                #raise NotImplementedError
        children = filter(bla,children) 
        """
        super(ShelTree,self).__init__(node,children)
        for child in self:
            #print(child)
            if not isinstance(child,basestring):
                child.set_parent(self)
    def parent(self):
        self._parent
        
    def set_parent(self, val):
        self._parent = val
        
    def sub_leaves(self):
        if len(self) > 0 and isinstance(self[0],basestring):
            return [self]
        else:
            leaves = []
            for child in self:
                leaves.extend(child.sub_leaves())
            return leaves
    def siblings(self):
        if self._parent is None: return []
        return self._parent.children
    def has_ancestor(self,ancestor,by_id = False):
        p = self._parent
        while p is not None:
            if by_id and id(p) == id(ancestor):
                return True 
            elif p == ancestor:
                return True
        return False

def respond(input_str):
    t = parser.nltk_parse(input_str)
    #print(t)
    input_tr = ShelTree.convert(t)
    #print(input_tr)
    return find_similar(input_tr)
    #TODO find similar grammar types as well as exact same grammar type

def debug_ex(c,*glob):
    print(glob)
    c.execute(*glob)

#https://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order
def ordered_uniquify(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]
    
def find_similar(tree):
    c = db.conn.cursor()
    goal = 5
    results = []
    shel_stack = tree.sub_leaves()
    while shel_stack and len(results) < goal:
        #print("shel_stack size")
        #print(len(shel_stack))
        item  = shel_stack.pop()
        idx = 1
        froms = ["FROM nodes n1 "]
        wheres= [" WHERE n1.is_input=1 AND n1.type=? AND n1.word=?"]
        paramss = [[ item.label(),item[0] ]]
        ancestry = [item]
        combinesql = lambda: (' '.join(froms))+(' '.join(wheres))
        while True:
            debug_ex(c,"SELECT COUNT(*) "+combinesql(),flatten(paramss))
            count = c.fetchone()[0]
            if (not ancestry[-1].parent()) or (not count):
                if not ancestry[-1].parent():
                    #froms.pop()
                    wheres.pop()
                    paramss.pop()
                    ancestry.pop()
                debug_ex(c,("SELECT n%d.rowid " % idx)+combinesql(),
                         flatten(paramss))
                for row in c.fetchall():
                    nodeid = get_top_node(row[0])
                    results.append(nodeid)
                break
            else:
                ancestry.append(ancestry[-1].parent())
            idx += 1
            froms.append(" JOIN nodes n%d "
                         "ON n%d.parent_id=n%d.rowid" % (idx,idx-1,idx))
            wheres.append(" AND n%d.type=?" % idx)
            paramss.append([ancestry[-1].label()])
    results.reverse()
    return ordered_uniquify(results)
