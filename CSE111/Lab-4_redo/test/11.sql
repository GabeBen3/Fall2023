.headers on

SELECT count(DISTINCT o_orderkey) as order_cnt
FROM (
        SELECT o_orderkey
        FROM (SELECT c_custkey
                FROM customer
                    WHERE c_acctbal < 0) c_cq, 
            orders
        WHERE o_custkey = c_custkey
    ),
    (
        SELECT l_orderkey 
        FROM (SELECT s_suppkey
            FROM supplier
            WHERE s_acctbal > 0) s_sq, 
        lineitem
        WHERE s_suppkey = l_suppkey
    )
WHERE (o_orderkey = l_orderkey);