from pricing import NewRelease, RegularPrice, ChildrensPrice

class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title: str, year: int, genre: list[str]):
        # Initialize a new movie.
        self.title = title
        self.year = None
        self.genres = None

    def is_genre(self, genre):
        return genre in self.genres

    def get_title(self):
        return self.title

    def __str__(self):
        return f"{self.title} ({self.year})"


