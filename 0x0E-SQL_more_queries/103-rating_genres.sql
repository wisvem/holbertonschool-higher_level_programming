-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT SUM(tv_show_ratings.rate) AS rating, tv_genres.name
FROM tv_shows, tv_show_ratings, tv_genres, tv_show_genres
WHERE tv_show_ratings.show_id=tv_shows.id
AND tv_genres.id=tv_show_genres.genre_id
AND tv_show_genres.show_id=tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC, tv_genres.name;