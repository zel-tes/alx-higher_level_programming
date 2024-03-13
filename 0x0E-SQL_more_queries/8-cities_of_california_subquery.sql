-- lists cities of califonia
SELECT states.id
FROM states
WHERE name = 'California'
UNION
SELECT id, name
FROM cities
WHERE id IN (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY cities.id ASC
