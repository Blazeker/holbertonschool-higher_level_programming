-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Display the temperature descending
SELECT city, AVG(value) as temp_avg FROM temperatures GROUP BY city ORDER BY temp_avg DESC;
