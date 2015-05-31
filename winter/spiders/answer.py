# -*- coding: utf-8 -*-
import scrapy
import pymongo
from scrapy import Spider
from scrapy.conf import settings
from winter.items import AnswerItem
from scrapy.selector import Selector


class PostsSpider(Spider):
  name = 'answer'
  allowed_domains = ['zhihu.com']

  connection = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
  db = connection[settings['MONGODB_DB']]    
  results = db.questions.find()
  start_urls = []
  for r in results:
    start_urls.append("http://www.zhihu.com" + r['url'])

  def parse(self, response):
    item = AnswerItem() 
    item['url'] = response.url
    item['question_title'] = response.xpath('//div[@id="zh-question-title"]//a[contains(@href,"question")]/text()').extract()[0]
    # todo 描述太长被折叠 & 富文本
    item['desc'] = ' '.join(response.xpath('//div[@id="zh-question-detail"]/div[@class="zm-editable-content"]/descendant::text()').extract())
    item['answer'] = ' '.join(response.xpath('//div[@id="zh-question-answer-wrap"]//div[@class="zm-item-rich-text"]/descendant::text()').extract())
    yield item