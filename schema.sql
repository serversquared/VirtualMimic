CREATE TABLE IF NOT EXISTS nodes
(
`parent` bigint,
`type` varchar(10),
`order` int
);

CREATE TABLE IF NOT EXISTS node_to_node
(
`input` bigint,
`response` bigint
);


