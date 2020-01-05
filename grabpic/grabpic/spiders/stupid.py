# -*- coding: utf-8 -*-
import scrapy
import sys
from grabpic.spiders import dymatic 
from scrapy_splash import SplashRequest
sys.path.append('../')
from grabpic import items

class stupid(scrapy.Spider):
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
        #item = items.GrabpicItem()
        for i in range(0, len(url_item)):
            #item['url']= url_item[i]
            
            #yield item
            print("-------------parse-------------")
            print(url_item[i])
            #print(item['url'])
            #print(item['name'])


