#DEBUG
# print(parse_log("/home/user/.xchat2/xchatlogs/FreeNode-##chat.log", "xchat2"))
# print(parse_log("/home/user/Desktop/lisp-2015-10.txt", "clozure", False))
# message_list = parse_dir("/home/user/Desktop/lisp-logs")
# print(message_list)
# print(len(message_list))

import stat_parser
import time
parser = stat_parser.Parser()
print("Started...")
start_time = time.time()
message_list = parse_dir("/home/joshypoo/Projects/VirtualMimic/logparse/TESTLOGS/")

for i, msg in enumerate(message_list):
    try:
        if i%10 == 0: print("iteration: {}".format(i))
        parser.parse(msg[1])
    except TypeError:
        print("{}: {}".format(i, msg[1]))

elapse_time = time.time() - start_time
print("elapse time: {}".format(elapse_time))
#EOF DEBUG
