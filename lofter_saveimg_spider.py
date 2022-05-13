# -*- coding: utf-8 -*-
"""
Created on 2022-05-13 15:00:12
---------
@summary:
---------
@author: Chiayen
"""

import feapder
from feapder.utils.log import log
import crawl_settings as Csettings
import string
import random
import datetime


class LofterSaveimgSpider(feapder.AirSpider):
    __custom_setting__ = dict(
        LOG_LEVEL = "INFO"
    )
    def next_page(self, page):
        url = Csettings.URL.format(page)
        return url

    def start_requests(self):
        page = 1
        url = self.next_page(page)

        yield feapder.Request(url, page=page, callback=self.parse)

    def parse(self, request, response):
        page = request.page

        artical_list = response.xpath('.//div[@class="content"]//div[@class="img"]//a/@href').extract()
        if artical_list:
            log.info('该页面 {url} 有 {index} 条文章'.format(url=request.url, index=len(artical_list)))
            page += 1
            for artiacl in artical_list:
                log.info('即将采集网页 {url} '.format(url=artiacl))
                yield feapder.Request(url=artiacl, callback=self.parse_detail)
        if page <= Csettings.PAGEMAX:
            url = self.next_page(page)
            yield feapder.Request(url, page=page, callback=self.parse)

    def parse_detail(self, request, response):
        url = request.url
        img_list = response.xpath('.//div[@class="content"]//div[@class="img"]//a/@bigimgsrc').extract()
        if img_list:
            for img in img_list:
                url = img.split('?')[0]
                yield feapder.Request(url, callback=self.save_img)
        else:
            log.info('该页面 {url} 无图片'.format(url=url))

    def save_img(self, request, response):
        filesuffix = request.url.split('.')[-1]
        filename = str(datetime.datetime.today().date()) + ' ' + self.get_redis_key(6)
        filepath = Csettings.SAVE_PATH + '/' + filename + '.' + filesuffix

        with open(filepath,'wb') as f:
            f.write(response.content)
            f.close()
        log.info('{url} 图片保存成功 文件名为 {filename}'.format(url =request.url,filename=filename))

    def get_redis_key(self, i):
        chars = string.ascii_letters + string.digits
        return ''.join(random.sample(chars, i))  # 得出的结果中字符不会有重复的


if __name__ == "__main__":
    LofterSaveimgSpider().start()
#     print(datetime.datetime.today().date())
