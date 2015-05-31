# coding: utf-8
from scrapy import Spider
from scrapy.selector import Selector
from winter.items import QuestionItem



class ZhihuSpider(Spider):
    name = "q_test"
    allowed_domains = ["http://www.zhihu.com/"]
    start_urls = [
        "http://www.zhihu.com/people/winter-25/answers",
    ]
    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="zm-item"]/h2')
 
        for question in questions:
            item = QuestionItem()
            item['question'] = question.xpath(
                'a[@class="question_link"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question_link"]/@href').extract()[0]
            yield item