from pricing import PriceStrategy
from dataclasses import dataclass
from typing import Collection

@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    price_strategy: PriceStrategy
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


