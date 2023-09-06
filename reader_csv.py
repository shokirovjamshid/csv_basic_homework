from csv import reader
def reader_csv(file_name):
    f = open(file_name)
    data_reader = list(reader(f))
    return data_reader