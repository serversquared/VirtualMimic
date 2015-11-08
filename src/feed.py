import sqlite3
from parser import parser

def feedSent_recursive(tree_seg, parent_id=None):
    #TODO
    pass
            

def feed(sentence, response, weight):
    parser = stat_parser.Parser()

    sent_tree = parser.parse(sentence)
    resp_tree = parser.parse(response)

    # Index nodes of sentence.
    feedSent_recursive(sent_tree)

    #TODO: do something with resp_tree


# test
feed("This is a sentence that has words in it.", "Shutup Roger.", 1)


# initialize database
# feed -> index into database
