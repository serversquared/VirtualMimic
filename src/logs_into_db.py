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
