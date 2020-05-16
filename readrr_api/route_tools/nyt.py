from json import loads

from decouple import config
from requests import get

# IMPORT CONNECTION

class NYT:

    def __init__(self):
        self.NYT_KEY = config('NYT_KEY')

    def get_lists(self):
        request_url = f'https://api.nytimes.com/svc/books/v3/lists/names.json?'\
            f'api-key={self.NYT_KEY}'
        request = get(request_url)
        return loads(request.text)

    def get_books(self, list_type):
        request_url = f'https://api.nytimes.com/svc/books/v3/lists/current/'\
            f'{list_type}.json?api-key={self.NYT_KEY}'
        request = get(request_url)
        return loads(request.text)
    
    def update(self):
        # MAY WANT TO IMPORT FROM ELSEWHERE
        return

    def get(self, book_list):
        # GET CURRENT RESULTS FROM DB
        return
