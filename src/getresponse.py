import random
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
    words = []
    cursor = db.conn.cursor()
    cursor.execute("SELECT rowid, word, type FROM nodes WHERE parent_id=?", (par_id,))
    for row in cursor.fetchall():
        print(row)
        if row[2] == "WORD":
            words.append(row[1])
        else:
            newWords = constrSen_recurser(row[0])
            for w in newWords:
                words.append(w)
    cursor.close()

    return words

# Constructs a sentence
def constrSen(sen_id):
    cursor = db.conn.cursor()
    cursor.execute("SELECT rowid, word, type FROM nodes WHERE rowid=?", (sen_id,))
    row = cursor.fetchone()
    if row == None:
        raise BadSentenceError('bad sentence ID: {}'.format(sen_id))
    if row[2] != "WORD":
        words = constrSen_recurser(sen_id)
    else:
        words = [row[1]]
    cursor.close()

    sentence = ""
    for w in words:
        sentence += w + ' '

    return sentence

def findResponseID(input_id):
    cursor = db.conn.cursor()
    cursor.execute("SELECT input, response, weight FROM nodes_to_nodes WHERE input=?", (input_id,))
    row = cursor.fetchone()
    return row[1]
"""    totalWeight = 0
    responses = []
    for row in cursor.fetchall():
        totalWeight += row[2]
        responses.append((row[1], row[2]))
    weightLimit = random.uniform(0, totalWeight)
    weightSum = 0
    print(len(responses))
    for resp in responses:
        weightSum += resp[1]
        resp_id = resp[0]
        if weightSum >= weightLimit:
            break

    cursor.close()

    return resp_id"""

def getResponse(input_id):
    try:
        resp_id = findResponseID(input_id)
        print(resp_id)
        sentence = constrSen(resp_id)
    except TypeError as e:
        raise BadSentenceError("bad sentence: {}".format(e))

    return sentence

