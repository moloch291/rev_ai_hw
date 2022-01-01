import os
import sys
sys.path.append("..")
from variable_storage import string_factory as str_f


class Display:

    @staticmethod
    def clean_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_main_menu():
        print(str_f.LOGO, "\n", str_f.MAIN_MENU_HEADER)

    @staticmethod
    def present_result(result, search_key=None, second_key=None):
        print(str_f.RESULT_HEADER, "\n")
        line_number = 1
        output = ""
        for line in result:
            output += f"""{str(line_number)}: {
                str(line[search_key]) if search_key is not None else line
            } {
               ": " + str(line[second_key]) if second_key is not None else ""
            }\n"""
            line_number += 1
        print(output)
