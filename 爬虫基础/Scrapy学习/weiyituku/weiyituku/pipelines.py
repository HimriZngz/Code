# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from scrapy.pipelines.images import ImagesPipeline  # 下载图片的管道
from scrapy.http import Request
from scrapy.exceptions import DropItem


class WeiyitukuPipeline(object):

    def creat_dir(self, path):
        exist = os.path.exists(path)
        if not exist:
            os.mkdir(path)

    def process_item(self, item, spider):
        '''
        保存链接信息到对应的文件夹
        '''
        path = "./images/" + item['title']
        pic_info_txt = path + '/' + item['title'] + '.txt'
        # 执行上面的文件夹创建
        self.creat_dir(path)

        # 如果已存在则先删除
        if os.path.exists(pic_info_txt):
            os.remove(pic_info_txt)

        # 将对应的信息写入文件
        with open(pic_info_txt, 'a')as f:
            for i in item['link']:
                f.write(i + '\n')

        return item


class WeiyitukuImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        print('已添加下载：%s\n' % item['title'])

        for i in item['link']:

            yield Request(i, meta={'title': item['title']})

    def file_path(self, request, response=None, info=None):
        # 从meta中获取标题文字
        title = request.meta['title']
        # 从链接中获取文件名
        name = request.url.split('/')[-1]
        # 拼接目录与文件名
        path_end = os.path.join(title, name)

        return path_end

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths

        # 下载完一个链接集就打印
        print('✬'*6, '已下载完成', '✬'*6, '\n%s\n共%s张' % (item['title'], item['number']))

        return item
