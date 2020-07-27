import pandas as pd
import exceptions



def file_contains_isbn(isbn, file_path, file_format, isbn_column_name):
    if file_format == 'csv':
        df = pd.read_csv(file_path)


    elif file_format == 'xlsx':
        df = pd.read_excel(file_path)


    else:
        raise exceptions.InvalidFileFormat('FILE_FORMAT should either be "csv" or "xlsx". ')


    try:
        isbns = df[isbn_column_name].astype(str)
        if isbn in isbns.unique():
            return True
        return False

    except KeyError:
        raise exceptions.InvalidColumn('Check the column name of csv file and make sure it matches ISBN_COLUMN_NAME')



