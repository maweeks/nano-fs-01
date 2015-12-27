import fresh_tomatoes
import media

#movieX = media.Movie("Name", "Storyline", "Poster Link", "Trailer Link")
avengers_age_of_ultron = media.Movie("Avengers: Age of Ultron", "Another epic adventure with Tony Stark and Bruce Banner.", "http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/avengers-movie-poster-1.jpg", "https://www.youtube.com/watch?v=bMP-FLmiIM0")

home = media.Movie("Home (2015)", "Aliens invade earth and think they can run the place...", "http://www.impawards.com/2015/posters/home_ver2_xlg.jpg", "https://www.youtube.com/watch?v=MyqZf8LiWvM")

inside_out = media.Movie("Inside Out (2015)", "A view of the battles inside the mind of a child while moving house...", "http://screenrant.com/wp-content/uploads/inside-out-poster.jpg", "https://www.youtube.com/watch?v=seMwpP0yeu4")

jurassic_world = media.Movie("Jurassic World", "Another jurassic park is created, though this time just bringing the dinosaurs back to life wasn't enough.", "http://e.movie.as/p/217255.jpg", "https://www.youtube.com/watch?v=RFinNxS5KN4")

mission_impossilbe_rogue_nation = media.Movie("Mission Impossible - Rogue Nation", "Another impossible mission that turns out to only be nearly impossible.", "http://static.srcdn.com/slir/w786-h1226-q90-c786:1226/wp-content/uploads/mission-impossible-rogue-nation-poster-tom-cruise.jpg", "https://www.youtube.com/watch?v=gOW_azQbOjw")

star_wars_vii = media.Movie("Star Wars: The Force Awakens", "More galactic warfare with lightsabers and storm troopers that can't shoot straight.", "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2015/10/star-wars-force-awakens-official-poster.jpg", "https://www.youtube.com/watch?v=sGbxmsDFVnE")

# print(inside_out.storyline);
# home.show_trailer();
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)

movies = [avengers_age_of_ultron, home, inside_out, jurassic_world, mission_impossilbe_rogue_nation, star_wars_vii]

# fresh_tomatoes.open_movies_page(movies)