from reader_csv import reader_csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    columns_len = len(data[0])
    return columns_len
# Read the csv file