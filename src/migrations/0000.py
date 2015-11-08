from yoyo import step
step("CREATE TABLE IF NOT EXISTS nodes
(
`parent_id` bigint,
`type` varchar(10),
`order` int,
`word` varchar(20)
);")
step("
CREATE TABLE IF NOT EXISTS nodes_to_nodes
(
`input` bigint,
`response` bigint,
`weight` double
);")
step("
CREATE INDEX IF NOT EXISTS awesome_index
ON nodes (`parent_id`,`order`);")
step("
CREATE INDEX IF NOT EXISTS cool_index
ON nodes_to_nodes (`input`, `response`);")
