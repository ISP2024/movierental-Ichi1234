from pricing import NewRelease, RegularPrice, ChildrensPrice

class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    NEW_RELEASE = NewRelease()
    REGULAR = RegularPrice()
    CHILDRENS = ChildrensPrice()


    def __init__(self, title, price_strategy):
        # Initialize a new movie.
        self.title = title
        self.price_strategy = price_strategy

    def get_title(self):
        return self.title

    def get_price_code(self):
        # get the price code
        return self.price_strategy

    def get_rental_points(self, days: int) -> float:
        return self.price_strategy.get_rental_points(days)

    def get_price(self, days :int) -> float:
        """Calculate the rental price."""
        return self.price_strategy.get_price(days)


    def __str__(self):
        return self.title


