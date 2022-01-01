import sys
sys.path.append("..")
from .. import query_storage as queries


class CoffeeMakerGetter:

    def __init__(self):
        self.count_of_props_w_coffee_m = self.__deifine_count()

    def get_count(self):
        return self.count_of_props_w_coffee_m

########################################################################################################################
    # Private method:
########################################################################################################################

    def __deifine_count(self):
        return queries.count_of_props_w_coffee_m()
