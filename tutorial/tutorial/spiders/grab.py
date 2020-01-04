import scrapy
from tutorial.spiders import dymatic 
from scrapy_splash import SplashRequest


class grab(scrapy.Spider):
    name = "grab"
    allowed_domains = ["1manhua.net"]
    url = "http://www.1manhua.net/manhua15840.html"
    url_1 = dymatic.get_total_session_url(url)
    for i in url_1
        print(i)
    start_urls = dymatic.get_total_session_url(url)

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'images':0,'timeout': 5})

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
