-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name
FROM cities, states
WHERE state_id = states.id and states.name = 'California'
