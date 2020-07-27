from requests_module import Request
import exceptions
from bs4 import BeautifulSoup
import requests
import pandas as pd

# For debugging delete it later
bs = BeautifulSoup

class GoodReadsScraper:

    origin_url = 'https://www.goodreads.com/'
    search_url = 'https://www.goodreads.com/search?q=%s&qid='

    def __init__(self, isbn, book_url = None):
        self.isbn = isbn
        #Optional
        self.book_url = book_url
        self.soup = None


    def get_resp(self,):
        resp = Request.get(self.search_url % (self.isbn))
        if resp:
            return resp
        else:
            raise exceptions.PageNotFound('Requests returned an error. Status code: %s' % (resp.status_code))




    def get_soup(self, resp):
        
        soup = BeautifulSoup(resp.text, 'lxml')
        
        return soup


    def get_book_details(self, resp_or_isbn):
        results = []
        
        
        if type(resp_or_isbn) == requests.models.Response:
            resp = resp_or_isbn
        
        else:
            self.isbn= resp_or_isbn
            resp = self.get_resp()
            
        
        soup =self.get_soup(resp)


        title = soup.find('h1', attrs = {'id' : 'bookTitle'})
        title = title.text.strip('\n ') if title else None

        authors_div = soup.find('div', attrs = {'id' : 'bookAuthors'})
        authors = authors_div.find_all('span', attrs = {'itemprop' : 'name'}) if authors_div else None
        authors_str = ''
        
        if authors:
            for i in range(len(authors)):
                text = authors[i].text if authors[i] else None
                if text:
                    authors_str += text + ';'
        
        else:
            authors_str = 'Not Found'
        
                

        average_rating = soup.find('span', attrs = {'itemprop' : 'ratingValue'}).text.strip('\n ') if soup.find('span', attrs = {'itemprop' : 'ratingValue'}) else None
        
        total_ratings_section = soup.find('meta', attrs = {'itemprop' : 'ratingCount'})
        total_ratings = total_ratings_section.attrs['content'] if total_ratings_section and 'content' in total_ratings_section.attrs  else None
        
    
        genres_dict = self.get_genres(soup)
        
        
    

        D = {'title' : title, 'average_rating' : average_rating, 'total_ratings' : total_ratings, 'authors' : authors_str}
        D.update(genres_dict)
        results.append(D)
        return pd.DataFrame(results)
    
    
    
    def get_genres(self, soup):
        key_name = 'genre_'
        genres_dict = dict()
            
        genres = soup.find_all('div', class_ = 'elementList')
        genres_list = [genre.a.text if genre.a else None for genre in genres]
            
        for i in range(len(genres_list)):
            genres_dict[key_name + str(i + 1)] = genres_list[i]
                
                
        return genres_dict
                
            
test_isbn = '9780786108619'
scraper = GoodReadsScraper(test_isbn)



