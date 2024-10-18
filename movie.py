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

    def __str__(self):
        return self.title


