import sys
sys.path.append("pyStatParser")
from stat_parser import Parser, display_tree

parser = Parser()

display_tree(parser.parse("I cannot decide what bottle of soda is the best"))
