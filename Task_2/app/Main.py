from util.Analyzer import Analyzer
from util.Display import Display


class Main:

    def __init__(self):
        self.__analyzer = Analyzer()

    def main(self):
        Display.print_decor()
        print("Task 2:\nQuality assessment of new dataset.\nRunning tests:")
        # Testing headers:
        if not self.__matching_headers() and self.__reassured("\nWant to check differences? [Y/N]\n"):
            non_common_columns = self.__analyzer.get_non_common_columns()
            print(non_common_columns)
        # Testing data types:
        Display.print_decor()
        if self.__reassured("\nWould like to verify each column of the database? [Y/N]\n"):
            d_type_check_result = self.__verify_by_column()
            print(d_type_check_result)
            print(
                f"Out of {str(d_type_check_result.count('Column'))} column(s)"
                f" {d_type_check_result.count('Same data type!')} matching!"
                f" {d_type_check_result.count('Data type is different!') - d_type_check_result.count('Not in test!')}"
                " column(s) represented, but with different data type."
            )


########################################################################################################################
    # Private methods:
########################################################################################################################

    def __verify_by_column(self):
        Display.clean_screen()
        Display.display_test_header("Run column tests:")
        return self.__analyzer.verify_columns()

    def __reassured(self, message):
        user_choice = input(message)
        if user_choice in ["n", "N", "no", "No"]:
            return False
        elif user_choice in ["y", "Y", "yes", "Yes"]:
            return True
        else:
            return self.__reassured(message)

    def __matching_headers(self):
        result = self.__analyzer.column_name_check()
        Display.display_test_header("Header test:")
        print(result)
        return result == "* Passed! *"
