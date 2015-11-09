from yoyo import step

step("""
UPDATE nodes
SET is_input=1
WHERE rowid
IN (SELECT input FROM nodes_to_nodes)
""")
step("""
UPDATE nodes
SET is_response=1
WHERE rowid
IN (SELECT response FROM nodes_to_nodes)
""")

''' #this doesn't work in sqlite
step("""UPDATE nodes n 
JOIN nodes_to_nodes n2n 
  ON n.rowid=n2n.response
SET n.is_response=1""",
     "UPDATE nodes SET is_response=0")
step("""UPDATE nodes n 
JOIN nodes_to_nodes n2n 
  ON n.rowid=n2n.input
SET n.is_input=1""",
     "UPDATE nodes SET is_input=0")
'''
