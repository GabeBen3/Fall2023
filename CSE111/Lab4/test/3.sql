.headers on

SELECT c_name, sum(o_totalprice)
FROM orders, customer, nation
WHERE o_orderdate BETWEEN '1996-01-01' AND '1996-12-31' AND
        o_custkey = c_custkey AND
            c_nationkey = n_nationkey AND 
                n_nationkey = 1
                    GROUP BY c_name;
    