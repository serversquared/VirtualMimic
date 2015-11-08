import sqlite3

import db
import stat_parser

class BadSentenceError(Exception):
    _msg = ''

    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg

def constrSen_recurser(par_id):
    sentence = ""
    cursor = db.conn.cursor()
    cursor.execute("SELECT rowid, word FROM nodes WHERE parent_id=?", (par_id,))
    for row in cursor:
        if row[1]:
            sentence += " " + row[1]
        else:
            sentence += " " + constrSen_recurser(row[0])
    cursor.close()

    return sentence

# Constructs a sentence
def constrSen(sen_id):
    cursor = db.conn.cursor()
    cursor.execute("SELECT rowid, word FROM nodes WHERE rowid=?", (sen_id,))
    row = cursor.fetchone()
    if row == None:
        raise BadSentenceError('bad sentence ID: {}'.format(sen_id))
    if not row[1]:
        sentence = constrSen_recurser(sen_id)
    else:
        sentence = row[1]
    cursor.close()

    return sentence

def getResponse(sentence):
    try:
        parser = stat_parser.Parser()
        tree = parser.parse(sentence)
        print(tree)
    except TypeError as e:
        raise BadSentenceError("bad sentence: {}".format(e))

    return "TODO: PLACE HOLDER"


#TODO: test constrSen()
