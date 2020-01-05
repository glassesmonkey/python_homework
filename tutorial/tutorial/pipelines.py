# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class TutorialPipeline(ImagesPipeline):
    #发生图片下载请求
    def get_media_requests(self, item, info):
        # for image_url in item['url']:
        #     print('------------image-url------')
        #     print('--------'+item['url']+' ------')
        #     print('----image----'+image_url+'------')
        #     # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
        #     yield scrapy.Request(image_url, meta={'item': item})
         yield scrapy.Request(item['url'], meta={'item': item})



    def file_path(self, request, response=None, info=None):
        print('----file path-------------')
        item = request.meta['item']
        image_name = item['url'].split('/')[-1]
        image_name2 = item['url'].split('/')[-2]
        #设置图片的路径
        #下载下来的图片名字就是这个图片页面的标题加这个图片的url最后一个'/'后面内容，因为这里每个图片的title不同，也可以直接写path = item['title']
        path = u'{}/{}'.format(image_name2, image_name)
        return path
