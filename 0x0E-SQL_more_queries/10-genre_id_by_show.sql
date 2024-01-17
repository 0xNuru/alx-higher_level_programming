-- This script lists all shows in hbtn_0d_tvshows that have genre

SELECT shows.title, genres.genre_id
FROM tv_shows as shows
JOIN tv_show_genres as genres
ON genres.show_id = shows.id
ORDER BY shows.title, genres.genre_id;
