## Weather Observation Station 5

SELECT CITY, LENGTH(CITY)

FROM STATION

ORDER BY LENGTH(CITY) ASC, CITY ASC

LIMIT 1;

SELECT CITY, LENGTH(CITY)

FROM STATION

ORDER BY LENGTH(CITY) DESC, CITY ASC

LIMIT 1;

---

## Weather Observation Station 6

SELECT DISTINCT CITY

FROM STATION

WHERE CITY REGEXP '^[aeiou]';

---

## Weather Observation Station 7

SELECT DISTINCT CITY

FROM STATION

WHERE CITY REGEXP '[aeiou]$';

---

## Weather Observation Station 8

SELECT DISTINCT CITY

FROM STATION

WHERE CITY REGEXP '^[aeiou]' AND CITY REGEXP '[aeiou]$';

- 위가 정답인데

SELECT DISTINCT CITY

FROM STATION

WHERE CITY REGEXP '^[aeiou]*[aeiou]$';

- 이건 왜 안되는지 모르겠음

---

## Weather Observation Station 9

SELECT DISTINCT CITY

FROM STATION

WHERE CITY REGEXP '^\[^aeiou]';

---

## Type of Triangle

SELECT

CASE

​    WHEN (A >= B+C) OR (B >= A+C) OR (C >= A+B) THEN 'Not A Triangle'

​    WHEN (A=B AND B=C AND C=A) THEN 'Equilateral'

​    WHEN A=B OR B=C OR C=A THEN 'Isosceles'

​    ELSE 'Scalene'

END

FROM TRIANGLES;

---

## The Blunder

SELECT CEIL(AVG(salary) - AVG(REPLACE(salary, '0', '')))

FROM EMPLOYEES;

---

## Top Earners

SELECT (salary * months) AS total, COUNT(*)

FROM Employee

GROUP BY total

ORDER BY total DESC

LIMIT 1;

---

## Average Population of Each Continent

ROUND() - 반올림

FLOOR() - 내림

CEIL() - 올림

---

## Draw The Triangle 1

??

---

## Draw The Triangle 2

??

