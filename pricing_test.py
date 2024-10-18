import unittest
from movie import Movie
from rental import Rental
from pricing import NewRelease, RegularPrice, ChildrensPrice

class PriceStrategyTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, ["Action", "Adventure", "Apocalypse"])
        self.childrens_movie = Movie("Air", 2023, ["History", "Children"])
        self.regular_movie = Movie("Frozen", 2016, ["Fantasy", "Let's it go", "Romance", "Disney"])

    def test_price_code(self):
        r = Rental(self.new_movie, 2)
        r.price_code_for_movie(self.new_movie)
        self.assertIsInstance(r.price_strategy, NewRelease)

        r = Rental(self.childrens_movie, 2)
        r.price_code_for_movie(self.childrens_movie)
        self.assertIsInstance(r.price_strategy, ChildrensPrice)

        r = Rental(self.regular_movie, 2)
        r.price_code_for_movie(self.regular_movie)
        self.assertIsInstance(r.price_strategy, RegularPrice)

