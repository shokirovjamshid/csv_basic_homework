from reader_csv import reader_csv
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    rows = int(data[-1][0])
    return rows
print(find_number_of_rows(reader_csv('data.csv')))
# Read the csv file
