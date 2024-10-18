import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", Movie.NEW_RELEASE)
        self.regular_movie = Movie("Air", Movie.REGULAR)
        self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", Movie.REGULAR)
        self.assertEqual("Air", m.get_title())
        self.assertEqual(Movie.REGULAR, m.get_price_code())

    def test_rental_price(self):
        rental = Rental(self.new_movie, self.new_movie.price_strategy, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, self.new_movie.price_strategy, 5)
        self.assertEqual(rental.get_price(), 15.0)
        #new test
        rental = Rental(self.new_movie, self.new_movie.price_strategy, 3)
        self.assertEqual(rental.get_price(), 9)
        rental = Rental(self.new_movie, self.new_movie.price_strategy, 10)
        self.assertEqual(rental.get_price(), 30.0)

    def test_rental_points(self):
        rental = Rental(self.new_movie, self.new_movie.price_strategy, 1)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, self.new_movie.price_strategy, 5)
        self.assertEqual(rental.get_rental_points(), 5)
        rental = Rental(self.new_movie, self.new_movie.price_strategy, 3)
        self.assertEqual(rental.get_rental_points(), 3)
        rental = Rental(self.new_movie, self.new_movie.price_strategy, 10)
        self.assertEqual(rental.get_rental_points(), 10)
