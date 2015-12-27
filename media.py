import webbrowser


class Video():
    """The class Video which stores a video's title and duration."""

    # Stores a list of the valid video ratings, currently unused.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Initialise a video object.
    def __init__(self, title, duration):
        # Initialise the video's variables.
        self.title = title
        self.duration = duration

    # A function to print the video's information.
    def show_info(self):
        print("Title: " + self.title)
        print("Duration: " + self.duration + " mins")


class Movie(Video):
    """The class Movie which stores a movie's title, duration
    created year, storyline, poster link and trailer link.
    Inherits from the Video class."""

    # Initialise a movie object.
    def __init__(self, movie_title, movie_duration, movie_year,
                 movie_storyline, movie_poster, movie_trailer):
        # Initialise a video object to inherit from.
        Video.__init__(self, movie_title, movie_duration)
        # Initialise the video's variables.
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    # A function to print the movie's information.
    # (Overides the Video function with the same name.)
    def show_info(self):
        print("Title: " + self.title)
        print("Duration: " + self.duration + " mins")
        print("Released: " + self.year)
        print("Storyline: " + self.storyline)
        print("Poster URL: " + self.poster_image_url)
        print("Trailer URL: " + self.trailer_youtube_url)

    # Opens a new browser window with the trailer URL provided.
    def show_trailer(self):
        webbrowser.open(self.trailer_url)


class TvShow(Video):
    """The class TvShow which stores a show's title and duration.
    Inherits from the Video class."""

    # Initialise a movie object.
    def __init__(self, tvshow_title, tvshow_duration):
        # Initialise a video object to inherit from.
        Video(self, tvshow_title, tvshow_duration)
