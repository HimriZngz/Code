# -*- coding: utf-8 -*-
import scrapy
from ..items import GouzhaizhiboItem


class ZhiboSpider(scrapy.Spider):
    name = 'zhibo'
    allowed_domains = ['zhibo.sogou.com']
    start_urls = ['https://zhibo.sogou.com/search.whtml?query=影视']

    def parse(self, response):
        print(response.url)

        info = GouzhaizhiboItem()

        # 全部房间对应的标签
        all_room = response.xpath('//div[@class="item game_right_dirk"]')

        for each in all_room:
            # 拿到房间平台、标题、链接
            room_title = each.xpath('./div[@class="msg2"]/p/a/text()').get()
            room_link = each.xpath('./div[@class="msg2"]/p/a/@href').get()
            room_plat = each.xpath('./div[@class="msg2"]/div[@class="msg-box"]/span/text()').get()

            info['plat'] = room_plat
            info['title'] = room_title
            info['link'] = room_link

            yield info

        # 翻页操作
        next_page = response.xpath('//div[@class="page-list"]/a[@class="page-next"]/@href').get()
        if next_page:
            next_url = response.urljoin(next_page)

            # 发出请求，调用自己
            yield scrapy.Request(next_url, callback=self.parse)


