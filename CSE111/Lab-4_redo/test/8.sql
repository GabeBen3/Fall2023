.headers on

SELECT count(DISTINCT o_clerk) as clerks
FROM lineitem, orders, supplier, customer, nation
WHERE l_orderkey = o_orderkey AND
        l_suppkey = s_suppkey AND 
            s_nationkey = n_nationkey AND 
                n_name = 'PERU';