# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 01:44:37 2020

@author: Piyush
"""

from isbn_checker import file_contains_isbn
from goodreads_scraper import GoodReadsScraper


######################## Fill the details below and run main() to start the program#############################
FILE_PATH = 'isbn.xlsx'
ISBN_COLUMN_NAME = 'ISBN'

# csv or xlsx
FILE_FORMAT = 'xlsx'


ISBN = '9781472367259'




def main():
    csv_has_isbn = file_contains_isbn(ISBN, FILE_PATH, FILE_FORMAT, ISBN_COLUMN_NAME)
    
    if not csv_has_isbn:
        scraper = GoodReadsScraper(ISBN)
        return scraper.get_book_details(ISBN)
    
    else:
        print('ISBN: %s found in the CSV File...' % (ISBN))
        return None
    

#csv_has_isbn = file_contains_isbn(ISBN, FILE_PATH, FILE_FORMAT, ISBN_COLUMN_NAME)











