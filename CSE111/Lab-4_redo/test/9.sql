.headers on

SELECT n_name as country, COUNT(DISTINCT o_orderkey) as cnt
FROM lineitem, orders, supplier, nation, region
WHERE l_orderkey = o_orderkey AND 
        o_orderdate BETWEEN '1993-01-01' AND '1993-12-31' AND
        o_orderstatus = 'F' AND 
        l_suppkey = s_suppkey AND 
            s_nationkey = n_nationkey AND 
                n_regionkey = r_regionkey AND
                    r_name = 'AFRICA'
                    GROUP BY n_name
                    HAVING COUNT(DISTINCT o_orderkey) > 200; 