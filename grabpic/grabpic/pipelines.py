# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class GrabpicPipeline(ImagesPipeline):
    #发生图片下载请求
    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['url']:
            # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
            yield scrapy.Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_name = item['url'].split('/')[-1]
        #设置图片的路径
        #下载下来的图片名字就是这个图片页面的标题加这个图片的url最后一个'/'后面内容，因为这里每个图片的title不同，也可以直接写path = item['title']
        # path = item['name'] + image_name
        path = u'{}/{}'.format(item['name'], image_name)
        return path