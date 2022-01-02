import pandas


class Analyzer:

    def __init__(self):
        self.__original_frame = pandas.read_csv("data/train.csv")
        self.__test_frame = pandas.read_csv("data/test.csv")

    def column_name_check(self):
        original_headers = [header for header in self.__original_frame.columns]
        test_headers = [header for header in self.__test_frame.columns]
        failed = f"* Failed! *\nVerified headers: {original_headers}\n\ndon't match: {test_headers}..."
        # If their length doesn't match, return False:
        if len(original_headers) != len(test_headers):
            return failed
        # Check if they are the same:
        else:
            return "* Passed! *" if sorted(test_headers) == sorted(original_headers) else failed

    def get_non_common_columns(self):
        lengths = [len(self.__original_frame), len(self.__test_frame)]
        # In case the length are the same but different:
        if lengths[0] == lengths[1]:
            return "The headers have the same length, but with different values..."
        # In case a frame has longer header:
        output = self.__get_output_for_size_diff(lengths)
        return output + "\n"

    def verify_columns(self):
        first_row_in_verified = self.__original_frame.iloc[0]
        first_row_in_test = self.__test_frame.iloc[0]

        output = ""
        column_number = 1
        for column in first_row_in_verified.keys():
            column_value_type_in_verified = str(type(first_row_in_verified[column]))
            output += "\n" + "* Column " + str(column_number) + ": '" + column + "' *" + "\nType: " + \
                      column_value_type_in_verified

            try:
                output_for_test = "\nRepresented in test!" if first_row_in_test[column] is not None \
                    else "\nNot in test!"
                type_in_test = str(type(first_row_in_test[column]))
            except KeyError:
                output_for_test = "\nNot in test!"
                type_in_test = "\nNone"

            type_output_for_test = "Same data type!" if column_value_type_in_verified == type_in_test \
                else "Data type is different!"
            output += output_for_test + "\n" + type_output_for_test + "\n"
            column_number += 1
        return output

########################################################################################################################
    # Private methods:
########################################################################################################################

    def __get_output_for_size_diff(self, lengths):
        # Decide which header list is longer and shorter:
        longer_header = "verified" if max(lengths) == len(self.__original_frame) else "test"
        shorter_header = "test" if longer_header == "verified" else "verified"
        # Get difference between the two header lists:
        difference = lengths[0] - lengths[1] if longer_header == "verified" else lengths[1] - lengths[0]
        # Get the extra column(s):
        extra_columns = str(set(self.__original_frame.columns).difference(self.__test_frame.columns)) \
            if longer_header == "verified" \
            else str(set(self.__test_frame.columns).difference(self.__original_frame.columns))
        # Return the output string:
        return f"The {longer_header} frame has {difference} extra column(s):" \
               f"\n* {extra_columns} is/are not represented in the {shorter_header} data!"
