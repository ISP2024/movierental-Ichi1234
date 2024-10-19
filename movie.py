import csv

from pricing import PriceStrategy, NewRelease, ChildrensPrice, RegularPrice
from dataclasses import dataclass
from typing import Collection

@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genres: Collection[str]

    def is_genre(self, genre: str) -> bool:
        """Check if the movie in genres."""
        return genre.lower() in (g.lower() for g in self.genres)

    def get_title(self):
        """GET the title of the movie."""
        return self.title

    def __str__(self):
        """Return the moview title and published year."""
        return f"{self.title} ({self.year})"


class MovieCatalog:
    _movie_data = None

    def __init__(self):
        # Initialize the catalog by parsing the CSV if it hasn't been done already
        if MovieCatalog._movie_data is None:
            self.parse_csv()
        else:
            self.data = MovieCatalog._movie_data

    def parse_csv(self):
        """Loop through csv."""
        with open("movies.csv", "r", encoding="UTF-8") as data_file:
            reader = csv.reader(data_file)

            for row in reader:
                if len(row) < 4 or not row[2].isnumeric() or row[0] in ["#id", "#", []]:
                    continue
                self.data.append(Movie(row[1], int(row[2]), row[3].split("|")))

            data_file.close()

    def get_movie(self, title, year=None):
        """Get Movie object."""
        for movie in self.data:
            if title.lower() == movie.title.lower() and not year:
                return movie
            elif title.lower() == movie.title.lower() and year == int(movie.year):
                return movie
        return False