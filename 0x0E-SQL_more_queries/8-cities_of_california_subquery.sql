-- lists cities of califonia
SELECT cities.id, cities.name
FROM cities
UNION
SELECT states_id 
FROM states
WHERE cities.states_id = (
	SELECT id
	FROM states
	WHERE name = California
)
ORDER BY cities.id ASC
