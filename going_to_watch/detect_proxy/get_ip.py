# -*- coding: utf-8 -*-
# !/usr/bin/env python

import scrapy
import urllib


class GetIp(scrapy.Request):
    name = 'get_ip'
    start_urls = (
        'http://www.xicidaili.com/nn/',
    )

    def parse(self, response):
        pass