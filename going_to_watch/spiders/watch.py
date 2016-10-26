# !/usr/bin/env python
# coding=utf-8


import scrapy
import json

from going_to_watch.items import GoingToWatchItem


class WatchMoive(scrapy.Spider):
    name = 'going'
    start_urls = (
        "http://1212.ip138.com/ic.asp",
    )

# https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=20
    def __init__(self):
        super(WatchMoive, self).__init__()
        self.type = 'movie'
        self.tag = '经典'
        self.sort = 'recommend'
        self.page_limit = 20
        self.page_start = 20

    # def parse(self, response):
    #   print response.xpath('//center/text()').extract()[0]


    def start_requests(self):
        url = 'https://movie.douban.com/j/search_subjects?'
        self.true_url = url + 'type=%s&tag=%s&sort=%s&page_limit=%s&page_start=%s' \
                         % (self.type, self.tag, self.sort, self.page_limit, self.page_start)
        print self.true_url
        return [scrapy.Request(self.true_url, callback=self.parse)]

    def parse(self, response):
        moive_info = json.loads(response.body, encoding='utf8')
        for moive in moive_info['subjects']:
             yield scrapy.Request(moive['url'], callback=self.get_info)

    def get_info(self, response):
        item = GoingToWatchItem()
        another_info = response.xpath('//div[@id="info"]/text()').re('\w+\(*\w*\)*')
        item['name'] = response.xpath('//div[@id="content"]/h1/span/text()').extract_first()
        bianju = response.xpath('//div[@class="subject clearfix"]/div[2]/span[2]/span[2]').re(">(\w+.\w+)</a>")
        item['daoyan'] = response.xpath('//div[@class="subject clearfix"]/div[2]/span[1]/span[2]/a/text()').extract_first()
        item['bianju'] = '/'.join(bianju)
        zhuyans = response.xpath('//div[@class="subject clearfix"]/div[2]/span[3]/span[2]/a/text()').extract()
        item['zhuyan'] = '/'.join(zhuyans)
        types = response.xpath('//span[@property="v:genre"]/text()').extract()
        item['type'] = '/'.join(types)
        item['distinct'] = another_info[0] if another_info[0] else None
        item['lamguage'] = another_info[1] if another_info[1] else None
        pub_dates = response.xpath('//span[@property="v:initialReleaseDate"]/text()').extract()
        item['pub_dte'] = '/'.join(pub_dates)
        item['time'] = response.xpath('//span[@property="v:runtime"]/text()').extract_first()
        item['another_name'] = '/ '.join(another_info[2:])
        item['score'] = response.xpath('//strong[@class="ll rating_num"]/text()').extract_first()
        item['juqing_jianjie'] = response.xpath('//span[@property="v:summary"]/text()').extract_first().split('\n')
        item['url'] = response.url
        yield item

