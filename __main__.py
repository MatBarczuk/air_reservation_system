from flight import Flight
from planes import *
from helpers import *


def make_flight():
    f = Flight('BA123', Boeing737())

    f.allocate_passenger('Elizabeth Brown', '24A')
    f.allocate_passenger('John Smith', '1B')
    f.allocate_passenger('George Snow', '1C')

    f.relocate_passenger('24A', '22G')

    f.print_cards(card_printer)


if __name__ == '__main__':
    make_flight()
