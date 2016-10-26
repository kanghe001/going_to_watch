# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import codecs
import json


class GoingToWatchPipeline(object):
    def process_item(self, item, spider):
        item = dict(item)
        json_data = json.dumps(item, ensure_ascii=False)
        result_file = codecs.open('./kanghe.json', 'a', encoding='utf-8')
        result_file.write(json_data + "\r\n")
        return item
