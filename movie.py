from abc import ABC, abstractmethod

class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return days

    def get_price(self, days):
        return 3 * days


class RegularPrice(PriceStrategy):

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return 1

    def get_price(self, days):
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children's movies."""

    def get_rental_points(self, days: int) -> int:
        return 1

    def get_price(self, days: int) -> float:
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

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


