import sys
sys.path.append("..")
from .. import query_storage as queries


class ResponseTimeGetter:

    def __init__(self):
        self.__unique_values = self.__get_unique_values_of_host_response_time()

    def get_unique_values(self):
        return self.__unique_values

########################################################################################################################
    # Private method:
########################################################################################################################

    def __get_unique_values_of_host_response_time(self):
        return queries.get_unique_response_time()

