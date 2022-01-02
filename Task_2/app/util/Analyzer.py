import pandas


class Analyzer:

    def __init__(self):
        self.__original_frame = pandas.read_csv("data/train.csv")
        self.__test_frame = pandas.read_csv("data/test.csv")

    def column_name_check(self):
        original_headers = [column for column in self.__original_frame.columns]
        test_headers = [column for column in self.__test_frame.columns]
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
        # ToDo: implement me!
        pass

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
