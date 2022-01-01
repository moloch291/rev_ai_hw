import sys
# import database queries:
sys.path.append("..")
from .. import query_storage as queries


class PriceGetter:

    def __init__(self):
        self.__avg_prices = self.__get_avg_per_neighbourhood()
        self.__avg_for_most_reviewed = self.__get_avg_for_most_reviewed()

    def get_avg_prices(self):
        return self.__avg_prices

    # I return the value string in a list since the Display object expects iterable:
    def get_avg_for_most_reviewed(self):
        return ["$" + str(self.__avg_for_most_reviewed[0]["avg_price"])]

########################################################################################################################
    # Private methods:
########################################################################################################################

    def __get_avg_for_most_reviewed(self):
        id_of_max_review = queries.find_most_reviewed()
        return queries.get_avg_of_most_reviewed(id_of_max_review["id"])

    def __get_avg_per_neighbourhood(self):
        neighbourhood_groups = queries.get_neighbourhood_groups()
        results = []
        for neighbourhood in neighbourhood_groups:
            neighbourhood_avg = str(queries.get_avg_price_of_group(neighbourhood["neighbourhood_group"])[0]['average'])
            results.append(
                {"neighbourhood_group": neighbourhood["neighbourhood_group"],
                 "avg_price": "$" + neighbourhood_avg}
            )
        return results

