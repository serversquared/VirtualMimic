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
    cursor.execute("SELECT rowid, word FROM nodes WHERE parent_id=?", (par_id,))
    for row in cursor:
        if row[1]:
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
    cursor.execute("SELECT rowid, word FROM nodes WHERE rowid=?", (sen_id,))
    row = cursor.fetchone()
    if row == None:
        raise BadSentenceError('bad sentence ID: {}'.format(sen_id))
    if not row[1]:
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
    totalWeight = 0
    responses = []
    for row in cursor:
        totalWeight += row[2]
        responses.append((row[1], row[2]))
    weightLimit = random.uniform(0, totalWeight)
    weightSum = 0
    for resp in responses:
        weightSum += resp[1]
        if weightSum >= weightLimit:
            break

    cursor.close()

    return resp[0]

def getResponse(sentence):
    try:
        '''
        parser = stat_parser.Parser()
        tree = parser.parse(sentence)
        '''
        #TODO: get input_id
        input_id = 1#DEBUG
        resp_id = findResponseID(input_id)
        sentence = constrSen(resp_id)
    except TypeError as e:
        raise BadSentenceError("bad sentence: {}".format(e))

    return sentence

