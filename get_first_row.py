from reader_csv import reader_csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
    """
   column_names = data[0]
   return column_names
# Read the csv file