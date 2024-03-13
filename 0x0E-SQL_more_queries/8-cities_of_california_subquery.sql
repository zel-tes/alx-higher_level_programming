-- lists cities of califonia
SELECT id, name
FROM cities
WHERE states.id = cities.states_id;
FROM states
ORDER BY cities.id ASC
FROM states
