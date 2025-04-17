import requests, json
from bs4 import BeautifulSoup
import requests, json
from bs4 import BeautifulSoup


HEADERS = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

class Tracker:

    def __init__(self,url):
        s = requests.Session()
        page = s.get(url, headers=HEADERS, verify=True) 
        self.soup = BeautifulSoup(page.text,"lxml")
        self.script = None
        for s in self.soup.find_all("script"):
            if 'pdpData' in s.text:
                self.script = s.get_text(strip=True)
                break


    def check_price(self,base_price):
        curr_price = json.loads(self.script[self.script.index('{'):])['pdpData']['price']['discounted']
        print(curr_price)
        if int(curr_price) <= int(base_price):
            return {'status':True}
        return {'status':False}

    def get_title(self):

        title = json.loads(self.script[self.script.index('{'):])['pdpData']['name']
        if title:
            return {'status':True, 'title':title}
        return {'status':False}

            
if __name__ == "__main__":

    t = Tracker('https://www.myntra.com/clothing-set/nauti-nati/nauti-nati-girls-pink-checked-top-with-shorts/16894906/buy')
    print(t.check_price(1490))
    print(t.get_title())

