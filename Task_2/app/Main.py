from util.Analyzer import Analyzer
from util.Display import Display

class Main:

    def __init__(self):
        self.__analyzer = Analyzer()

    def main(self):
        # Testing headers:
        matching_headers = self.__matching_headers()
        if not matching_headers and self.__reassured():
            common_columns = self.__analyzer.count_common_columns()
            print(common_columns)

########################################################################################################################
    # Private methods:
########################################################################################################################

    def __reassured(self):
        user_choice = input("\nWant to check type of common columns? [Y/N]\n")
        if user_choice in ["n", "N", "no", "No"]:
            return False
        elif user_choice in ["y", "Y", "yes", "Yes"]:
            return True
        else:
            return self.__reassured()

    def __matching_headers(self):
        Display.print_decor()
        print("Header test - see if columns match")
        Display.print_decor()

        result = self.__analyzer.column_name_check()
        print(result)
        return result == "* Passed! * "
