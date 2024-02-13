.headers on

SELECT count(*) as items
FROM lineitem, 
    (
        SELECT o_orderkey
        FROM (
                SELECT c_custkey 
                FROM customer, nation
                WHERE c_nationkey = n_nationkey AND
                        n_name = 'KENYA'
                ), orders
            WHERE o_custkey = c_custkey
    ), 
    (
        SELECT s_suppkey
        FROM supplier, nation, region
        WHERE s_nationkey = n_nationkey AND
                n_regionkey = r_regionkey AND
                    r_name = 'ASIA'
    )
WHERE l_orderkey = o_orderkey AND
        l_suppkey = s_suppkey;
