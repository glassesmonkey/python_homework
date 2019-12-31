import scrapy
#import dymatic_grab 


class grab(scrapy.Spider):
    name = "grab"
    allowed_domains = ["jianshu.com"]
    start_urls = ["https://www.jianshu.com/p/6bc5a4641629","https://www.jianshu.com"]


    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response)