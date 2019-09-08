# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Playstorev2Item(scrapy.Item):
    App = scrapy.Field()
    Developer = scrapy.Field()
    Rating = scrapy.Field()
    Price = scrapy.Field()
    Reviews = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    
