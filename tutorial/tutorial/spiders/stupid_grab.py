import scrapy
import sys
from tutorial.spiders import dymatic 
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup
import re
sys.path.append('../')
from tutorial import items

class stupid_grab(scrapy.Spider):
    name = "stupid"
    allowed_domains = ["1manhua.net"]
    url = ["http://www.1manhua.net/page278018/1.html?s=10"
    ,"http://www.1manhua.net/page278018/2.html?s=10"]




    def start_requests(self):
        #print("----start_requests-----")
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'images':0,'timeout': 5})

    def parse(self, response):
        url_item=dymatic.get_pic_url(response)
        item = items.GrabItem()
        for i in range(0, len(url_item)):
            item['url']= url_item[i]
            
            yield item
            print("-------------parse-------------")
            print(item['url'])
            #print(item['name'])

