#Define function,Get coloumn names from a csv file
from reader_csv import reader_csv
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    column_names = data[0]
    return column_names
print(get_column_names(reader_csv('data.csv')))    
# Read the csv file