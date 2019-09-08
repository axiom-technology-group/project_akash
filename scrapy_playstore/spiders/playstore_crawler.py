# -*- coding: utf-8 -*-
import scrapy
import csv
import os
from scrapy.http import Request
import requests
import bs4


class PlaystoreCrawlerSpider(scrapy.Spider):
    name = 'playstore_crawler'
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

    def scrape1(self,x):
        content = requests.get(x)
        parser = bs4.BeautifulSoup(content.text,"lxml")
        try:
            Website= parser.findAll('a',attrs={'rel':'nofollow'})[0]['href']
        except IndexError:
            Website = 'No Info!'
        return Website
    
    
    def scrape2(self,x):
        content = requests.get(x)
        parser = bs4.BeautifulSoup(content.text,"lxml")
        return parser.find('span',attrs={'class':'AYi5wd TBRnV'}).text
    
    
    def parse(self, response):
        
#         search_keyword=response.meta["search_text"]
#         for i in range(len(response.xpath("//div[@class='b8cIId ReQCgd Q9MA7b']//text()").extract())):
#                        Prices= response.xpath("//div[@class='LCATme']/span/span/text()").extract()[i]
#                        Title=  response.xpath("//div[@class='b8cIId ReQCgd Q9MA7b']//text()").extract()[i]
#                        Genre=  response.xpath("//div[@class='b8cIId ReQCgd KoLSrc']//text()").extract()[i]
                       
                    
                    
#                        No=i+1
#                        Prices=''.join(Prices).strip() 
#                        Title=''.join(Title).strip() 
#                        Genre=''.join(Genre).strip() 
        
#                        yield{
#                             'No':No,
#                             'Title':Title,
#                             'Prices':Prices,
#                             'Genre':Genre
#                             }
    
            
#         search_keyword=response.meta["search_text"]
        for i in range(len(response.xpath("//div[@class='WsMG1c nnK0zc']/text()").extract())):
            App= response.xpath("//div[@class='WsMG1c nnK0zc']/text()").extract()[i]
            Developer =  response.xpath("//div[@class='KoLSrc']/text()").extract()[i]
            Rating=  response.xpath("//div[@class='pf5lIe']/div/@aria-label").extract()[i][6:9]
            Price= response.xpath("//span[@class='VfPpfd ZdBevf i5DZme']/span/text()").extract()[i]
            Website=self.scrape1(''.join(self.allowed_domains)+response.xpath("//div[@class='b8cIId ReQCgd KoLSrc']/a/@href").extract()[i]) 
            Reviews=self.scrape2(''.join(self.allowed_domains)+response.xpath("//div[@class='b8cIId ReQCgd Q9MA7b']/a/@href").extract()[i])
            
                       
                       
                    
                    
            No=i+1
            App=''.join(App).strip() 
            Developer=''.join(Developer).strip() 
            Rating=''.join(Rating).strip()
            Reviews=''.join(Reviews).strip()
            Website=''.join(Website).strip()
            Price= ''.join(Price).strip()
        
            yield{
                            'No':No,
                            'App':App,
                            'Developer':Developer,
                            'Rating':Rating,
                            'Reviews':Reviews,
                            'Website':Website,
                            'Price':Price
                 }
            
#         url1="https://play.google.com"
#         for i in response.xpath("//div[@class='W9yFB']/a/@href").extract():
#             yield scrapy.Request(url1+i, callback = self.parse_next, dont_filter=False)
            
#     def parse_next(self, response):
#         a=response.xpath("//span[@class='htlgb']/a/@href").extract_first()  
#         yield {
#             'a':a
#         }

    
#          for i in range(len(response.xpath("//div[@class='b8cIId ReQCgd Q9MA7b']//text()").extract())):
#                 Prices= response.xpath("//div[@class='LCATme']/span/span/text()").extract()[i]
#                 Title=  response.xpath("//div[@class='b8cIId ReQCgd Q9MA7b']//text()").extract()[i]
#                 Genre=  response.xpath("//div[@class='b8cIId ReQCgd KoLSrc']//text()").extract()[i]
                       
                    
                    
#                 No=i+1
#                 Prices=''.join(Prices).strip() 
#                 Title=''.join(Title).strip() 
#                 Genre=''.join(Genre).strip() 
        
#                 yield{
#                             'No':No,
#                             'Title':Title,
#                             'Prices':Prices,
#                             'Genre':Genre
#                      }
        
        
