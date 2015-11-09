import random

import getresponse as gr
import produce_response as pr
from parser import parser

print("\n")
print("Talk to the bot!")
line = ""
while line not in ('q','quit','x','exit','Q','X'):
    line = raw_input("Chat:")
    result_list = pr.respond(line)
    result = result_list.pop()
    #choose a random one, heavily weighing ones near the beginning
    while random.randrange(4) != 0:
        result = result_list.pop()
    print(gr.getResponse(result))
