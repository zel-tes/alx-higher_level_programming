-- count no of shows
SELECT tv_genres.name AS "genre", COUNT(tv_show_genres.show_id) AS "number_of_shows"
FROM tv_genres LEFT OUTER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id WHERE (
	SELECT tv_shows.id 
	FROM tv_shows
	WHERE tv_show_genres.show_id = tv_shows.id
)
GROUP BY tv_genres.name
