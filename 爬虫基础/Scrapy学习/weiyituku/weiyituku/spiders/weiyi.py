# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import WeiyitukuItem


class WeiyiSpider(scrapy.Spider):
    name = 'weiyi'
    allowed_domains = ['mmonly.cc']
    start_urls = ['http://www.mmonly.cc/mmtp/']

    info = WeiyitukuItem()
    links = []

    def parse(self, response):
        '''
        拿全部主文章链接
        '''
        all_div = response.xpath('//div[@class="item masonry_brick masonry-brick"]')
        for each_div in all_div:
            each_type = each_div.xpath('.//div[@class="items_comment"]/a[last()]/text()').get()

            if str(each_type) != '美女明星' and '清纯美女':
                # 拿到大标题、主链接
                # title = each_div.xpath('.//div[@class="title"]/span/a/text()').get()
                url = each_div.xpath('.//div[@class="title"]/span/a/@href').get()

                # 用re拿每一篇中存在的图片数量
                other = each_div.xpath('.//div[@class="items_likes"]/text()').get()
                other_match = re.match('.*?共(\d+)张', other)
                number = other_match.group(1)

                # print(title)
                # print(url)
                # print(number)

                yield scrapy.Request(url, callback=self.get_link)

    def get_link(self, response):
        # 下载原图链接
        link = response.xpath('//li[@class="pic-down h-pic-down"]/a/@href').get()
        self.links.append(link)

        # 下一页按钮的残缺型链接
        next_page = response.xpath('//div[@class="pages"]//li[@id="nl"]/a/@href').get()
        if next_page != '##':
            # 从当前链接抽取前缀并与获得的残缺链接相连，生成下一页的完整链接
            this_url = response.url
            add = this_url.split('/')[-4:-1]
            new_next_page = 'http://%s/%s/%s/%s' % (add[0], add[1], add[2], next_page)

            yield scrapy.Request(new_next_page, callback=self.get_link)
        else:
            title = response.xpath('//h1/text()').get()
            number = response.xpath('//h1//span[@class="totalpage"]/text()').get()
            self.info['title'] = title
            self.info['number'] = number
            self.info['link'] = self.links

            yield self.info







