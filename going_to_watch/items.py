# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoingToWatchItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    daoyan = scrapy.Field()
    bianju = scrapy.Field()
    zhuyan = scrapy.Field()
    type = scrapy.Field()
    distinct = scrapy.Field()
    lamguage = scrapy.Field()
    pub_dte = scrapy.Field()
    time = scrapy.Field()
    another_name = scrapy.Field()
    score = scrapy.Field()
    juqing_jianjie = scrapy.Field()
    url = scrapy.Field()

