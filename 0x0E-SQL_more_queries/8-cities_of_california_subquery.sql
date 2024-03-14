-- lists cities of califonia
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
	SELECT states.id 
	FROM states
	WHERE name = 'California'
)
ORDER BY cities.id ASC
