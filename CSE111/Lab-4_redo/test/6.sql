.headers on

-- How many unique parts produced by every supplier
--  in INDONESIA are ordered at every priority? Print
-- the supplier name, the order priority, and the number of parts.

SELECT s_name as supplier, o_orderpriority as priority, COUNT(DISTINCT p_partkey) as parts
FROM supplier, orders, part, nation, partsupp, lineitem
WHERE s_nationkey = n_nationkey AND 
        p_partkey = l_partkey AND 
            l_orderkey = o_orderkey AND 
                l_suppkey = ps_suppkey AND 
                    ps_suppkey = s_suppkey AND 
                        n_name = 'INDONESIA'
                GROUP BY s_name, o_orderpriority;

