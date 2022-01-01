import sys
from .Display import Display
# Get unique strings:
sys.path.append("..")
from variable_storage import string_factory as str_f


class Input:

    @staticmethod
    def ask_for_int(message):
        try:
            return int(input(message))
        except ValueError:
            Display.clean_console()
            print(str_f.TYPE_ERROR_INT_MENU)
            return Input.ask_for_int(message)

    @staticmethod
    def ask_for_string(message):
        try:
            return str(input(message))
        except ValueError:
            Display.clean_console()
            print("Please provide text input!")
            Input.ask_for_string(message)
