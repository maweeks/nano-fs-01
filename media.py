import webbrowser

class Video():
    """Docs and stuff..."""
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_info(self):
        print("Title: " + self.title)

class Movie(Video):
    """This is my documentation..."""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_duration, movie_year, movie_storyline, movie_poster, movie_trailer):
        Video.__init__(self, movie_title, movie_duration)
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_url)


class TvShow(Video):
    """This is my other documentation..."""

    def __init__(self, tvshow_title, tvshow_duration):
        Video(tvshow_title, tvshow_duration)