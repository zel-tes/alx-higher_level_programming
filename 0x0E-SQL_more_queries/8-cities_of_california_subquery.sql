-- lists cities of califonia
SELECT id, name
FROM cities
WHERE (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY cities.id ASC
