#!/usr/bin/python2

"""
TODO:
 * learn from user as they talk to the bot
"""

import os.path
import sqlite3
import sys

import db
import getresponse
import logparse.logparse as logparse
import sentence_into_db as sid

EXCEPTION_LIMIT = 10

def getNumBetween(msg, first, last):
    # first and last are inclusive
    while True:
        num = raw_input(msg)
        print('')
        try:
            num = int(num)
        except ValueError:
            print("Not a valid integer")
            print("Try again\n")
            continue
        if not first <= num <= last:
            print("Number too small [{}, {}]".format(first, last))
            print("Try again\n")
        else:
            return num

while True:
    print('Options:')
    print(' * (f)eed')
    print(' * (t)alk')
    print(' * (q)uit\n')

    option = raw_input('Enter an option: ')
    print('')

    if option == 'f':
        while True:
            loc = raw_input('Enter a text file or directory of text files to feed: ')
            print('')

            if os.path.isfile(loc):
                logs = logparse.parse_log(loc)
                break
            elif os.path.isdir(loc):
                logs = logparse.parse_dir(loc)
                break
            else:
                print('Invalid file/directory path')
                print('Try again\n')

        yesno = raw_input('Do you want to limit the number of feeds? (y/N): ')
        if yesno.lower() == 'y':
            feedCnt = getNumBetween('Enter number of feeds to do [{}, {}]: '.format(1, len(logs)),
                                    1, len(logs))
            logs = logs[:feedCnt]

        print('Feeding (this will probably take awhile)...')
        prev = None
        exceptCount = 0
        prematureBreak = False
        for line in logs:
            if not prev is None:
                try:
                    sid.feed(prev[1],line[1])
                except KeyboardInterrupt:
                    sys.exit(0)
                    exceptCount = 0
                except Exception as e:
                    print(e)
                    prev = None
                    exceptCount += 1
                    if exceptCount >= EXCEPTION_LIMIT:
                        prematureBreak = True
                        break
            prev = line
        if prematureBreak:
            print('Feeding cutoff prematurely\n')
        else:
            print('Done feeding\n')

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
                    print("Do not worry about this")
                    print("Just try again\n")

    elif option == 'q':
        sys.exit(0)

    else:
          print("Invalid option: {}\n".format(option))
end
