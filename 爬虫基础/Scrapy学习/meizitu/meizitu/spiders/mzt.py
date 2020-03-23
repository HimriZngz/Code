# -*- coding: utf-8 -*-
import scrapy
from ..items import MeizituItem

"""
2020年3月13日 被封ip了，代理后，依旧抓取出错
2020年3月14日 解封，但是图片链接被重定向302
"""


class MztSpider(scrapy.Spider):
    name = 'mzt'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/']

    info = MeizituItem()

    def parse(self, response):
        """
        在主要页拿到每篇图的url
        """
        ul_tag = response.xpath('//ul[@id="pins"]/li')
        for li_tag in ul_tag:
            url = li_tag.xpath('./span[1]/a/@href').get()
            title = li_tag.xpath('./span[1]/a/text()').get()
            time = li_tag.xpath('./span[@class="time"]/text()').get()
            # print(title, '\n', url, '\n', time)

            self.info['title'] = time + '_' + title
            self.info['url'] = url
            self.info['link'] = []

            yield scrapy.Request(url, callback=self.get_link)

        next_button = response.xpath('//div[@class="nav-links"]/a[@class="next page-numbers"]')
        if next_button is not None:
            next_url = next_button.xpath('./@href').get()
            # print(next_url)
            # yield scrapy.Request(next_url, callback=self.parse)

    def get_link(self, response):
        """
        在详情页拿到每张图的link
        """
        link = response.xpath('//div[@class="main-image"]/p/a/img/@src').get()
        self.info['link'].append(link)
        print(link)

        next_page = response.xpath('//div[@class="pagenavi"]/a[last()]/span/text()').get()
        if next_page.find('下一页') != -1:
            next_link = response.xpath('//div[@class="pagenavi"]/a[last()]/@href').get()
            yield scrapy.Request(next_link, callback=self.get_link)
        else:
            print(self.info['link'])
            # yield self.info
