.headers on

SELECT n_name as country, count(c_custkey) as cnt
FROM orders, customer, nation, region
WHERE o_custkey = c_custkey AND 
        c_nationkey = n_nationkey AND 
            n_regionkey = r_regionkey AND 
                r_name = 'EUROPE'
                GROUP BY n_name;
