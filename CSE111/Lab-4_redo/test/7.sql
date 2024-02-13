.headers on

SELECT n_name as country, o_orderstatus as status, count(*) as orders
FROM orders, customer, nation
WHERE o_custkey = c_custkey AND
    c_nationkey = n_nationkey AND
        n_regionkey = 0
        GROUP BY o_orderstatus, n_name
        ORDER BY n_name;