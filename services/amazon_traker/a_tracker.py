from flask import jsonify
import requests
from bs4 import BeautifulSoup
import re

url = "https://www.amazon.in/dp/B08FF2CKMB/ref=cm_sw_r_cp_apa_i_0R4G5CN63D57DTWZW22X?_encoding=UTF8&psc=1"


HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
# HEADERS = {
# 'authority': 'www.amazon.com',
# 'pragma': 'no-cache',
# 'cache-control': 'no-cache',
# 'dnt': '1',
# 'upgrade-insecure-requests': '1',
# 'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'sec-fetch-site': 'none',
# 'sec-fetch-mode': 'navigate',
# 'sec-fetch-dest': 'document',
# 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
# }


class Tracker:

    def __init__(self,url):
        self.url = url
        s = requests.Session()
        page = s.get(url, headers=HEADERS)
        self.soup = BeautifulSoup(page.content, 'html.parser')



    def check_price(self,base_price):
        curr_price = self.soup.find("span", {"class": "a-price-whole"})
        print(curr_price)
        # print(self.soup)
        # curr_price = "".join(re.findall(r'\b\d+\b', curr_price))
        # if( int(curr_price) <= int(base_price)): 
        #     return {"status":True}
        return {'status':False}
        
    
    def get_title(self):
        title = self.soup.find("span", {"class": "product-title-word-break"}).get_text()
        if title:
            return {"status":True,"title":title}
        return {"status":False}




if __name__ ==  "__main__":

    t = Tracker("https://www.amazon.in/MANSH-Womens-Jacquard-Blouse-BLTR11_Red/dp/B08CDZSKV2/ref=sr_1_1_sspa?crid=35KQKUSW7T1U5&keywords=saree&qid=1652519370&sprefix=saree%2Caps%2C372&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExR1IyMVlQVjY3Rk40JmVuY3J5cHRlZElkPUEwNjUxNDY3MkI0RTQ0WFhINFFFSCZlbmNyeXB0ZWRBZElkPUEwNDIyNjY0MldJQVlHODExU1RTSiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1")
    
    price = t.check_price(20)
    print(price)


