import os


class Display:

    @staticmethod
    def print_decor():
        print("########################################")

    @staticmethod
    def clean_console():
        os.system('cls' if os.name == 'nt' else 'clear')
