import sys
from get_top_node import get_top_node
if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    arg = 3459
print(get_top_node(arg))
