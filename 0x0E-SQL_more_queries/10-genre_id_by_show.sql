-- This script lists all shows in hbtn_0d_tvshows that have genre

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres as genres
JOIN tv_shows as shows
ON genres.show_id = shows.id
ORDER BY shows.title, genres.genre_id;
