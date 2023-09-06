from reader_csv import reader_csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    column = []
    for i in data:
        column.append(i[0])
    return column   
# Read the csv file