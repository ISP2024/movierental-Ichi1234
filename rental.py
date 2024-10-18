from movie import Movie
from datetime import datetime
from pricing import NewRelease, ChildrensPrice, RegularPrice

class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    
    def __init__(self, movie: Movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.price_strategy = None
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def price_code_for_movie(self, movie):
         """Set price code for movie"""
         if datetime.now().year == movie.year:
             self.price_strategy = NewRelease()
         elif "Children" in movie.genres:
             self.price_strategy = ChildrensPrice()
         else:
             self.price_strategy = RegularPrice()

    def get_price_code(self):
        """Get the price code."""
        return self.price_strategy

    def get_days_rented(self):
        return self.days_rented

    def get_price(self) -> float:
        """Calculate the rental price."""
        return self.price_strategy.get_price(self.get_days_rented())

    def get_rental_points(self):
        return self.price_strategy.get_rental_points(self.get_days_rented())