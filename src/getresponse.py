class BadSentenceError(Exception):
    def __init__(self, msg):
        _msg = msg

    def __str__(self):
        print(_msg)

def getResponse(sentence):
    try:
        #TODO
        pass
    except TypeError as e:
        raise BadSentenceError("bad sentence: {}".format(e))

    return "TODO: PLACE HOLDER"
