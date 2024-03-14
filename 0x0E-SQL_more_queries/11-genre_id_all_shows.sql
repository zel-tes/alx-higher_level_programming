-- lists all show geners
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT OUTER JOIN tv_show_genres
ON tv_shows.ID = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
