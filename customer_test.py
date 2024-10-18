import re
import unittest 
from customer import Customer
from pricing import NewRelease, RegularPrice, ChildrensPrice
from rental import Rental
from movie import Movie

class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", NewRelease(), 2024, ["War", "Female Lead", "Action", "Jwizzed"])
        self.regular_movie = Movie("CitizenFour", RegularPrice(), 2021, ["FOUR", "Citizen"])
        self.childrens_movie = Movie("Frozen", ChildrensPrice(), 2016, ["Yes", "let", "it",
                                                                        "go", "fantasy", "adventure"])

    @unittest.skip("No convenient way to test")
    def test_billing():
        # no convenient way to test billing since its buried in the statement() method.
        pass
    
    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, self.new_movie.price_strategy, 4)) # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_compute_total_amount(self):
        self.c.add_rental(Rental(self.new_movie, self.new_movie.price_strategy, 4))  # days
        amount1 = self.c.compute_total_amount()
        self.assertEqual(12, amount1)

        self.c.add_rental(Rental(self.new_movie, self.new_movie.price_strategy, 4))  # days
        amount2 = self.c.compute_total_amount()
        self.assertEqual(24, amount2)



