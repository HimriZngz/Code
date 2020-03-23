# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class XicidailispiderPipeline(object):

    def open_spider(self, spider):
        self.file = open('ip_info.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        info = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.file.write(info)

        return item
