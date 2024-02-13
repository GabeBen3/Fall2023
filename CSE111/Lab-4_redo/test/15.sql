.headers on
-- Find the supplier with the largest account 
--balance in every region. Print the region name, the supplier
-- name, and the account balance.

SELECT r_name as region, s_name as supplier, MAX(s_acctbal) as acct_bal
FROM supplier s
JOIN nation n ON s.s_nationkey = n.n_nationkey
JOIN region r ON n.n_regionkey = r.r_regionkey
GROUP BY r_name;
