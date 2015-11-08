from os import listdir
from os.path import isfile, join

def parse_message(message, logformat):
    splitmessage = message.split()
    if logformat == "xchat2":
        if splitmessage[0] == "****" or splitmessage[3] == "*":
            return False
        else:
            sender = splitmessage[3][1:-1]
            message = " ".join(splitmessage[4:])
            return sender, message
    elif logformat == "clozure":
        if len(splitmessage) <= 2 or (splitmessage[1][-1] != ":" and splitmessage[1][-1] != ">"):
            return False
        elif splitmessage[1][-1] == ">":
            sender = splitmessage[1][1:-1]
            message = " ".join(splitmessage[2:])
            return sender, message
        elif splitmessage[1][-1] == ":":
            sender = splitmessage[1][:-1]
            message = " ".join(splitmessage[2:])
            return sender, message


def parse_log(logfile, logformat, old_message_list):
    message_list = []
    linenum = 0
    if old_message_list:
        message_list = old_message_list
    last_message = ()
    with open(logfile) as f:
        try:
            for line in f:
                linenum = linenum + 1
                # print(linenum)
                if line != "\n":
                    message = parse_message(line, logformat)
                    if message:
                        if (last_message and last_message[0] != message[0]) or not last_message:
                            last_message = message
                            message_list.append(message)
        except UnicodeDecodeError as err:
            print("Unicode Error: " + str(err) + " in " + logfile + " line " + str(linenum))
            # raise
    return message_list

def parse_dir(dirpath):
    files = [f for f in listdir(dirpath) if isfile(join(dirpath,f))]
    message_list = []
    for file in files:
        message_list = parse_log(dirpath + "/" + file, "clozure", message_list)
    return message_list

#print(parse_log("/home/user/.xchat2/xchatlogs/FreeNode-##chat.log", "xchat2"))
# print(parse_log("/home/user/Desktop/lisp-2015-10.txt", "clozure", False))
message_list = parse_dir("/home/user/Desktop/lisp-logs")
print(message_list)
print(len(message_list))