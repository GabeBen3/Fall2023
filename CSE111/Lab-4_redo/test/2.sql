.headers on

SELECT c_name as customer, count(c_name) as cnt
FROM orders, customer, nation
WHERE o_orderdate BETWEEN '1992-01-01' AND '1992-12-31' AND
         o_custkey = c_custkey AND
            c_nationkey = n_nationkey AND 
            n_nationkey = 4
            GROUP BY c_name;
