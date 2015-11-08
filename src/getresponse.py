import sqlite3

import stat_parser

class BadSentenceError(Exception):
    _msg = ''

    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg

def getResponse(sentence):
    try:
        parser = stat_parser.Parser()
        tree = parser.parse(sentence)
        #TODO
        pass
    except TypeError as e:
        raise BadSentenceError("bad sentence: {}".format(e))

    return "TODO: PLACE HOLDER"
