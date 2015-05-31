# -*- coding: utf-8 -*-

import scrapy
from scrapy.item import Item, Field

class QuestionItem(scrapy.Item):
  question = Field()
  url = Field()

class AnswerItem(scrapy.Item):
	url = Field()
	question_title = Field()	
	desc = Field()
	answer = Field()