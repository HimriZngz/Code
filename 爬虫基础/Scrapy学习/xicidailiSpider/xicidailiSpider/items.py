# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XicidailispiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    ip = scrapy.Field()             # ip地址
    port = scrapy.Field()           # 端口
    address = scrapy.Field()        # 物理地址
    speed = scrapy.Field()          # 连接速度
    connect_time = scrapy.Field()   # 连接时间
    life_time = scrapy.Field()      # 存活时间
    check_time = scrapy.Field()     # 验证时间

