# !/usr/bin/env python
# coding=utf-8

import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import urllib


class WatchMiddlewares(UserAgentMiddleware):
    agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"

    # proxy_ip = ['183.57.17.194:8081', '14.29.124.52:80', '61.153.104.71:138']

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.agent)
        # ip = random.choice(self.proxy_ip)
        # print "http://" + ip
        # request.meta['proxy'] = "http://" + ip


