import scrapy
import sys
from tutorial.spiders import dymatic 
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup
import re
sys.path.append('../')
from tutorial.items import TutorialItem

class grab(scrapy.Spider):
    name = "grab"
    allowed_domains = ["1manhua.net","164.94201314.net"]
    url = "http://www.1manhua.net/manhua27411.html"
    start_urls = dymatic.get_total_session_url(url)
    #start_urls = 
    

    def start_requests(self):
        print("----start_requests-----")
        # print(self.start_urls)
        for url in self.start_urls:
            print(url)
            yield SplashRequest(url, callback=self.parse, args={'images':0,'timeout': 5})

    def parse(self, response):
        # (url_item,name_item)=dymatic.get_total_page(response)
        # item = items.GrabItem()
        # for i in range(0, len(url_item)):
        #     item['url']= url_item[i]
        #     item['name'] = name_item[i]
        #     yield item
        #     print(item['url'])
        #     #print(item['name'])
        
        url_item=dymatic.get_pic_url(response)
        
        item = TutorialItem()
        
        for i in range(0, len(url_item)):
            
            item['url']= url_item[i]
            print("-------------parse333-------------")
            print(item['url'])
            yield item 
            print("-------------parse444-------------")
           
            #print(item['name'])

