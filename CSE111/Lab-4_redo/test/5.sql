.headers on

SELECT n_name as country, count(n_name) as cnt
FROM supplier, nation
WHERE s_nationkey = n_nationkey AND 
        (n_nationkey = 1 OR n_nationkey = 2)
            GROUP BY n_name;