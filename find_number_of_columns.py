from csv import reader
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    f = open(data)
    data_reader = list(reader(f))
    columns_len = len(data_reader[0])
    return columns_len
print(find_number_of_columns('data.csv'))
# Read the csv file