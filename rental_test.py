import unittest
from pricing import NewRelease, ChildrensPrice, RegularPrice
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, ["Action", "Adventure", "Apocalypse"])
        self.regular_movie = Movie("Air", 2023, ["History", "James Brucker"])
        self.childrens_movie = Movie("Frozen", 2016, ["Fantasy", "Let's it go", "Romance", "Disney"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2023, ["History", "James Brucker"])
        self.assertEqual("Air", m.get_title())
        self.assertEqual("Air (2023)", str(m))

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        rental.price_code_for_movie(self.new_movie)
        self.assertEqual(rental.get_price(), 3.0)

        rental = Rental(self.new_movie, 5)
        rental.price_code_for_movie(self.new_movie)
        self.assertEqual(rental.get_price(), 15.0)
        #new test
        rental = Rental(self.new_movie, 3)
        rental.price_code_for_movie(self.new_movie)
        self.assertEqual(rental.get_price(), 9)

        rental = Rental(self.new_movie, 10)
        rental.price_code_for_movie(self.new_movie)
        self.assertEqual(rental.get_price(), 30.0)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 1)
        rental.price_code_for_movie(self.new_movie)
        self.assertEqual(rental.get_rental_points(), 1)

        rental = Rental(self.new_movie, 5)
        rental.price_code_for_movie(self.new_movie)
        self.assertEqual(rental.get_rental_points(), 5)
        rental = Rental(self.new_movie, 3)
        rental.price_code_for_movie(self.new_movie)
        self.assertEqual(rental.get_rental_points(), 3)

        rental = Rental(self.new_movie, 10)
        rental.price_code_for_movie(self.new_movie)
        self.assertEqual(rental.get_rental_points(), 10)
