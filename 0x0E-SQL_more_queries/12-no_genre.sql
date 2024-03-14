-- lists shows with no genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT OUTER JOIN tv_show_genres
ON tv_show_genres.genre_id = NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
