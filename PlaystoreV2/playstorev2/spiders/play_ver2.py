# -*- coding: utf-8 -*-
import scrapy
import csv
import os
from scrapy.http import Request
import requests
import bs4
from playstorev2.items import Playstorev2Item


class PlayVer2Spider(scrapy.Spider):
    name = 'play_ver2'
    allowed_domains = ['https://play.google.com']
    start_urls = ['http://https://play.google.com/']
    
    
    
    def start_requests(self):
        """Read keywords from keywords file amd construct the search URL"""

        with open(os.path.join(os.path.dirname(__file__), "../resources/keywords.csv")) as search_keywords:
            for keyword in csv.DictReader(search_keywords):
                search_text=keyword["keyword"]
                url="https://play.google.com/store/{0}".format(search_text)
                # The meta is used to send our search text into the parser as metadata
#                 for i in range(len(response.xpath("//div[@class='W9yFB']/a/@href").extract())):
                yield scrapy.Request(url, callback = self.parse)
#                 , meta = {"search_text": search_text})

    def parse(self, response):
        
        item= Playstorev2Item()
        for i in range(len(response.xpath("//div[@class='WsMG1c nnK0zc']/text()").extract())):
            item['App']= response.xpath("//div[@class='WsMG1c nnK0zc']/text()").extract()[i]
            item['Developer'] =  response.xpath("//div[@class='KoLSrc']/text()").extract()[i]
            item['Rating']=  response.xpath("//div[@class='pf5lIe']/div/@aria-label").extract()[i][6:9] 
            item['Price']= response.xpath("//span[@class='VfPpfd ZdBevf i5DZme']/span/text()").extract()[i]           
            
            item['App']=''.join(item['App']).strip() 
            item['Developer']=''.join(item['Developer']).strip() 
            item['Rating']=''.join(item['Rating']).strip()
            item['Price']= ''.join(item['Price']).strip()
            meta = {'item': item}
            url1=''.join(self.allowed_domains)+response.xpath("//div[@class='b8cIId ReQCgd Q9MA7b']/a/@href").extract()[i]
            
            yield Request(url1, meta=meta, callback=self.parse_item_2,dont_filter=True)
        
        
    def parse_item_2(self, response):
        item = Playstorev2Item(response.meta['item'])
        item['Reviews']=response.xpath("//span[@class='AYi5wd TBRnV']/span/text()").extract()
            
        yield item
        
            
#             yield item
