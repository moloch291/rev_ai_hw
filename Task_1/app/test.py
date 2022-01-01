import pandas as pd


def number_of_airbnbs_via_pandas():
    data = pd.read_csv("../CSVs/listings_complex.csv", index_col=0)
    filtered_frame = data[data["amenities"].str.contains("coffee")]
    return len(filtered_frame)


print("Number of lines: ", str(number_of_airbnbs_via_pandas()))
