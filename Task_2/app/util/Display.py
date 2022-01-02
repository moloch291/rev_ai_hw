import os


class Display:

    @staticmethod
    def print_decor():
        print("###############################################")

    @staticmethod
    def clean_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_test_header(message):
        Display.print_decor()
        print(message)
        Display.print_decor()
