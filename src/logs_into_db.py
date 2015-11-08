import sys
import os.path
import logparse.logparse as logparse
import sentence_into_db as sid

EXCEPTION_LIMIT = 10

start = int(sys.argv[1])
stop  = int(sys.argv[2])
loc   = sys.argv[3]

if os.path.isfile(loc):
    logs = logparse.parse_file(loc)
else:
    logs = logparse.parse_dir(loc)

logs_filtered = logs[start:stop]

prev = None
exceptCount = 0
prematureBreak = False
for line in logs_filtered:
    if not prev is None:
        try:
            sid.feed(prev[1],line[1])
            exceptCount = 0
            prev = line
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            print(e)
            print("(On log line {})".format(line[2]))
            prev = None
            exceptCount += 1
            if exceptCount >= EXCEPTION_LIMIT:
                prematureBreak = True
                break
    else:
        prev = line

if prematureBreak:
    print('Feeding cutoff prematurely\n')
else:
    print('Done feeding\n')
