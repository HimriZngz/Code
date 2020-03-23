# -*- coding: utf-8 -*-
import scrapy
from ..items import XicidailispiderItem


class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['xicidaili.com']
    # start_urls = [f'https://www.xicidaili.com/nn/{page}' for page in range(1, 11)]
    start_urls = ['https://www.xicidaili.com/nn/']

    def parse(self, response):
        print(response.url)

        trs = response.xpath('//tr[@class]')
        for tr in trs:
            ip_info = XicidailispiderItem()
            ip = tr.xpath('./td[2]/text()').get()
            port = tr.xpath('./td[3]/text()').get()
            address = tr.xpath('./td[4]/a/text()').get()
            speed = tr.xpath('./td[7]/div/@title').get()
            connect_time = tr.xpath('./td[8]/div/@title').get()
            life_time = tr.xpath('./td[9]/text()').get()
            check_time = tr.xpath('./td[10]/text()').get()

            print('\'%s:%s\',' % (ip, port))

            ip_info['ip'] = ip
            ip_info['port'] = port
            ip_info['address'] = address
            ip_info['speed'] = speed
            ip_info['connect_time'] = connect_time
            ip_info['life_time'] = life_time
            ip_info['check_time'] = check_time

            # yield ip_info

            # yield {
            #     'ip地址': ip,
            #     '端口号': port,
            #     '位于': address,
            #     '连接速度': speed,
            #     '连接时间': connect_time,
            #     '存活时间': life_time,
            #     '检查时间': check_time
            # }
