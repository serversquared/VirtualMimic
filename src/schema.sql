CREATE TABLE IF NOT EXISTS nodes
(
`parent_id` bigint,
`type` varchar(10),
`order` int,
`word` varchar(20)
);

CREATE TABLE IF NOT EXISTS nodes_to_nodes
(
`input` bigint,
`response` bigint,
`weight` double
);


