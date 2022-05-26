-- Q1 --

(select first_name from customer)
UNION
(select first_name from actor)


-- Q2 --

(select first_name from customer)
INTERSECT
(select first_name from actor)

-- Q3 --

(select first_name from customer)
EXCEPT
(select first_name from actor)

-- Q4 --

(select first_name from customer)
INTERSECT ALL
(select first_name from actor)

(select first_name from customer)
UNION ALL
(select first_name from actor)

(select first_name from customer)
EXCEPT ALL
(select first_name from actor)