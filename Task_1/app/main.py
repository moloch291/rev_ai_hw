import sys
import time
from variable_storage import string_factory as str_f
from variable_storage import magic_numbers as mgc_n
from interact.Input import Input
from interact.Display import Display
from database_handler.data_handlers.PriceGetter import PriceGetter
from database_handler.data_handlers.ResponseTimeGetter import ResponseTimeGetter
from database_handler.data_handlers.CoffeeMakerGetter import CoffeeMakerGetter


def exit_program():
    print(str_f.GOOD_BYE_MESSAGE)
    time.sleep(mgc_n.SLEEPING_TIME_SEC)
    sys.exit(mgc_n.INITIAL_STATE)


def reload():
    enter = Input.ask_for_string(str_f.ASK_FOR_ENTER)
    if enter == "":
        Display.clean_console()
        main()
    reload()


def run_sub_functions(user_choice):
    price_getter = PriceGetter()

    if user_choice == 1:
        prices = price_getter.get_avg_prices()
        Display.present_result(prices, "neighbourhood_group", "avg_price")
    elif user_choice == 2:
        resp_time_getter = ResponseTimeGetter()
        unique_values = resp_time_getter.get_unique_values()
        Display.present_result(unique_values, "host_response_time")
    elif user_choice == 3:
        avg_price_of_most_reviewed = price_getter.get_avg_for_most_reviewed()
        Display.present_result(avg_price_of_most_reviewed)
    elif user_choice == 4:
        counter = CoffeeMakerGetter()
        number_of_props = counter.get_count()
        Display.present_result(number_of_props, "count")
    elif user_choice == 5:
        exit_program()
    else:
        print(str_f.TYPE_ERROR_INT_MENU)
        reload()


def main():
    # Choosing functionality:
    Display.display_main_menu()
    user_choice = Input.ask_for_int(str_f.MAIN_MENU_OPTIONS)
    # Obtaining and presenting the data:
    run_sub_functions(user_choice)
    reload()


if __name__ == "__main__":
    Display.clean_console()
    main()
