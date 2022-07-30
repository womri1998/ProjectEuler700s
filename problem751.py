from math import floor
from decimal import Decimal


THETHA = Decimal(2.956938891377988)


def next_b(previous: Decimal) -> Decimal:
    return floor(previous) * (previous % 1 + 1)


def concatenation(thetha: Decimal) -> Decimal:
    string = f'{floor(thetha)}.'
    while len(string) < 28:
        thetha = next_b(thetha)
        string += f"{floor(thetha)}"
    return Decimal(string)


def binary_search(low: Decimal = Decimal(2), high: Decimal = Decimal(2.99)) -> Decimal:
    while low <= high:
        thetha = (high + low) / 2
        sequence = concatenation(thetha)
        if sequence > thetha:
            low = thetha
        elif sequence < thetha:
            high = thetha
        else:
            return thetha
    pass


if __name__ == "__main__":
    print(str(binary_search())[:26])
