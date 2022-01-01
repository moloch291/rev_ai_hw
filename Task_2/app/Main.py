from util.Analyzer import Analyzer
from util.Display import Display


class Main:

    def __init__(self):
        self.__analyzer = Analyzer()

    def main(self):
        Display.print_decor()
        print("Task 2:\nQuality assessment of new dataset.\nRunning tests:")
        # Testing headers:
        if not self.__matching_headers() and self.__reassured("\nWant to check type of common columns? [Y/N]\n"):
            common_columns = self.__analyzer.count_common_columns()
            print(common_columns)
        # Testing data types:
        if self.__reassured("\nWould like to verify each column?\n"):
            self.__verify_by_column()

########################################################################################################################
    # Private methods:
########################################################################################################################

    def __verify_by_column(self):
        # ToDo: implement me!
        return

    def __reassured(self, message):
        user_choice = input(message)
        if user_choice in ["n", "N", "no", "No"]:
            return False
        elif user_choice in ["y", "Y", "yes", "Yes"]:
            return True
        else:
            return self.__reassured(message)

    def __matching_headers(self):
        Display.print_decor()
        result = self.__analyzer.column_name_check()

        print("Header test:")
        print(result)
        return result == "* Passed! * "
