from yoyo import step

step("""CREATE INDEX IF NOT EXISTS better_index
ON nodes (type,word);""")
