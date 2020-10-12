from pprint import pprint

from flight import Flight
from planes import *
from helpers import *


def make_flight():
    f = Flight('BA123', Boeing737())
    # print(f.get_airlines())
    # print(f.get_number())
    # print(f.get_airplane_model())
    #
    # b = Boeing737()
    # print(b.num_seats())
    #
    # a = AirbusA370()
    # print(a.num_seats())

    f.allocate_passenger('Lech K', '24A')
    f.allocate_passenger('Jarosław K', '1B')
    f.allocate_passenger('Paweł K', '1C')

    f.relocate_passenger('24A', '22G')

    pprint(f.num_empty_seats())

    f.print_cards(card_printer)

    # pprint(f.seating_plan)


if __name__ == '__main__':
    make_flight()
