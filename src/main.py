import os.path
import sqlite3
import sys

import db
import getresponse
import logparse.logparse as logparse
import sentence_into_db as sid

while True:
    print('Options:')
    print(' * (f)eed')
    print(' * (t)alk')
    print(' * (q)uit\n')

    option = raw_input('Enter an option: ')
    print('')

    if option == 'f':
        path = raw_input('Enter a text file or directory of text files to feed: ')
        '''
        import sys
        import os.path
        import logparse.logparse as logparse
        import sentence_into_db as sid

        start = int(sys.argv[1])
        stop  = int(sys.argv[2])
        loc   = sys.argv[3]

        if os.path.isfile(loc):
            logs = logparse.parse_file(loc)
        else:
            logs = logparse.parse_dir(loc)

        logs_filtered = logs[start:stop]

        prev = None
        for line in logs_filtered:
        if not prev is None:
        try:
            sid.feed(prev[1],line[1])
        except TypeError as e:
            print(e)
        prev = line
        '''

    elif option == 't':
        while True:
            sentence = raw_input('Enter a sentence (q to quit): ')
            print('')
            if not sentence:
                print("Please enter words")
                print("Try again\n")
            if len(sentence) == 1 and sentence.lower() == 'q':
                print('')
                break
            else:
                try:
                    print("Bot: {}\n".format(getresponse.getResponse(sentence)))
                except getresponse.BadSentenceError as e:
                    print("ERROR: {}".format(e))
                    print("Try again\n")

    elif option == 'q':
        sys.exit(0)

    else:
          print("Invalid option: {}\n".format(option))
end
