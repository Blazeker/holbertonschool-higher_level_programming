-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- list all the tv shows
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows_genres INNER JOIN tv_shows
ON tv_show_genres.show_id=tv_shows.id ORDER BY tv_shows.title, tv_shows_genres.genre_id ASC;