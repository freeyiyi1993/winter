# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule

from winter.items import QuestionItem

class QuestionCrawlerSpider(CrawlSpider):
    name = 'question'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://www.zhihu.com/people/winter-25/answers'] 

    rules = (
        Rule(LinkExtractor(allow='zhihu\.com/people/winter\-25/answers\?page=\d+$'), 
            'parse_item', follow=True
        ),
    )

    def parse_item(self, response):
        questions = Selector(response).xpath('//div[@class="zm-item"]/h2')
        
        for question in questions:
            item = QuestionItem()
            item['question'] = question.xpath(
                'a[@class="question_link"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question_link"]/@href').extract()[0]
            yield item
    