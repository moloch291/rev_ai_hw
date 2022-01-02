import sys
# import database queries:
sys.path.append("..")
from .. import query_storage as queries
sys.path.append("../../../..")
from variable_storage import magic_numbers as mgc_n


class PriceGetter:

    def __init__(self):
        self.__avg_prices = self.__get_avg_per_neighbourhood()
        self.__avg_for_most_reviewed = self.__get_avg_for_most_reviewed()

    def get_avg_prices(self):
        return self.__avg_prices

    # I return the value string in a list since the Display object expects iterable:
    def get_avg_for_most_reviewed(self):
        return ["$" + str(self.__avg_for_most_reviewed["avg_price"])]

########################################################################################################################
    # Private methods:
########################################################################################################################

    def __get_avg_for_most_reviewed(self):
        return queries.get_avg_of_most_reviewed()

    def __get_avg_per_neighbourhood(self):
        return queries.get_avg_per_neighbourhood_groups()
