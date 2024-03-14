-- lists cities of califonia
SELECT id, name
FROM cities
WHERE EXISTS (
	SELECT 1
	FROM states
	WHERE name = 'California'
)
ORDER BY cities.id ASC
