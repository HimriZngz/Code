# -*- coding: utf-8 -*-
import scrapy
import logging
from ..items import YouzhaishetupianItem


class YzsSpider(scrapy.Spider):
    name = 'yzs'
    allowed_domains = ['youzhaishe.com']
    start_urls = ['https://www.youzhaishe.com/meitu/', 'https://www.youzhaishe.com/meitu/page/2',
                  'https://www.youzhaishe.com/meitu/page/3', 'https://www.youzhaishe.com/meitu/page/4', ]

    def parse(self, response):

        logging.warning('出现了一个警告')

        # 拿到全部的篇幅名字和链接
        main_page = response.xpath('//div[@class="list-item"]')
        for page in main_page:
            title = page.xpath('.//h3[@class="post__title typescale-2 xin-underline"]/a/text()').get()
            link = page.xpath('.//h3[@class="post__title typescale-2 xin-underline"]/a/@href').get()

            yield scrapy.Request(link, callback=self.get_pic)

        ### 动态获取下一页的方法没想出来 ###
        # # 拿到下一页按钮的链接
        # next_page = response.xpath('//div[@class="mnmd-pagination__links text-center"]/a[last()]/@href').get()
        # # 判断下下一页的a标签的href属性是不是个正常的链接
        # if next_page.startswith('https://www.youzhaishe.com/meitu/page/'):
        #
        #     yield scrapy.Request(next_page, callback=self.parse)

    def get_pic(self, response):

        pic_info = YouzhaishetupianItem()

        # 当前篇幅的主链
        url = response.url

        pic_info['url'] = url

        # 拿标题
        title = response.xpath('//header[@class="single-header"]/h1[@class="entry-title"]/text()').get()

        pic_info['title'] = title

        # 拿前3个p标签的img
        links = []
        # div = response.xpath('//div[@class="entry-content typography-copy"]')
        #         # img1 = div.xpath('./p[1]/img[@class="aligncenter"]/@src').get()
        #         # img2 = div.xpath('./p[2]/img[@class="aligncenter"]/@src').get()
        #         # img3 = div.xpath('./p[3]/img[@class="aligncenter"]/@src').get()
        #         #
        #         # links.append(img1)
        #         # links.append(img2)
        #         # links.append(img3)
        #         #
        #         # # 拿第四个p标签的img
        #         # p4 = div.xpath('./p[4]')
        #         # for i in p4:
        #         #     imgs = i.xpath('./img[@class="aligncenter"]/@src')
        #         #     for img in imgs:
        #         #         # 依次将get()出来的链接加入
        #         #         links.append(img.get())
        p_tag = response.xpath('//p')
        for p in p_tag:
            img_tag = p.xpath('./img[@class="aligncenter"]/@src')
            for imgs in img_tag:
                img = imgs.get()
                if not img.startswith('https://xiaoshuoxitongxiaozong') and img.startswith('https://ae01.alicdn.com'):
                    links.append(img)

        pic_info['link'] = links

        yield pic_info


