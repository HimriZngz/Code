# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.pipelines.images import ImagesPipeline  # 下载图片的管道
from scrapy.utils.project import get_project_settings   # 导入设置
from scrapy.http import Request
from scrapy.exceptions import DropItem


class MeizituPipeline(object):
    def process_item(self, item, spider):
        return item


class MeizituImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        print(item['link'])
        print('已添加下载：%s\n' % item['title'])

        for i in item['link']:

            # meta用来向file_path函数附带发送信息，以便使用item对象的属性或值
            # ！！！！！！注意meta的内容以及file_path函数中title的获取代码！！！！！！！！！！！！！！！
            yield Request(i, meta={'title': item['title']})

    def file_path(self, request, response=None, info=None):
        # 从meta中获取标题文字
        title = request.meta['title']

        path = "./images/" + title
        exist = os.path.exists(path)
        if not exist:
            os.mkdir(path)

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
        print('✬'*6, '已下载完成', '✬'*6, '\n%s\n' % item['title'])

        return item
