import csv
import logging

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

    def __init__(self):
        # Initialize the catalog by parsing the CSV if it hasn't been done already
        self.logger = logging.getLogger("MovieCatalog")
        self.logger.setLevel(logging.DEBUG)
        self.logging_handler()

        # Initialize movie generator
        self.movie_generator = self.parse_csv()
        self.data = []

    def logging_handler(self):
        """Add Handler to self.logger."""
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)

    def parse_csv(self):
        """Loop through csv."""
        with open("movies.csv", "r", encoding="UTF-8") as data_file:
            reader = csv.reader(data_file)

            for row in reader:
                if len(row) < 4 or not row[2].isnumeric() or row[0] in ["#id", "#", []]:
                    self.logger.debug(f"Unrecognized format {row}")
                    continue
                yield Movie(row[1], int(row[2]), row[3].split("|"))

            data_file.close()

    def get_movie(self, title, year=None):
        """Get Movie object."""
        for movie in self.data:
            if title.lower() == movie.title.lower() and not year:
                return movie
            elif title.lower() == movie.title.lower() and year == int(movie.year):
                return movie

        for movie in self.movie_generator:
            self.data.append(movie)
            if movie.title.lower() == title.lower() and (year is None or movie.year == year):
                return movie

        return False
