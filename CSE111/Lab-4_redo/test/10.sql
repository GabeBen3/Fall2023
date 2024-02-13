.headers on

SELECT p_type as part_type, MIN(l_discount) as min_disc, MAX(l_discount) as max_disc
FROM lineitem, part
WHERE l_partkey = p_partkey AND 
        (p_type LIKE '%ECONOMY%' OR p_type LIKE '%COPPER%')
        GROUP BY p_type;
