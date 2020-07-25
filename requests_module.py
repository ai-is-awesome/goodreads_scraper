import requests

class Request(object):

    max_tries = 5

    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
    'accept-language': 'en-US,en;q=0.9', 
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',

    }



    def __init__(self):
        return None






    @classmethod
    def get(self, url):
        session = requests.session()
        resp = session.get(url, headers = self.headers)
        num_tries = 1
        while resp.status_code != 200 and  num_tries < self.max_tries:
            resp = session.get(url, headers=  self.headers)
            num_tries += 1

        if num_tries == self.max_tries:
            raise Exception("Max number of tries reached")

        return resp
            

    def post(self, url, data):

        session = requests.session()
        resp = session.post(data = data)
        return resp




