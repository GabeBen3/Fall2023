.headers on

SELECT s_name as supplier, count(s_suppkey) as cnt
FROM part, partsupp, supplier
WHERE p_partkey = p_partkey AND 
    substr(p_container, -3, 3) = 'BOX' AND
        p_partkey = ps_partkey AND 
            ps_suppkey = s_suppkey AND 
                s_nationkey = 14
                    GROUP BY s_suppkey;