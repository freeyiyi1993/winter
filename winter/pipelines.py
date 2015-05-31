# -*- coding: utf-8 -*-
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
 
 
class MongoDBPipeline(object):
  def __init__(self):
    connection = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
    db = connection[settings['MONGODB_DB']]
    self.questions = db[settings['MONGODB_COLLECTION_Q']]
    self.answers = db[settings['MONGODB_COLLECTION_A']]

  def process_item(self, item, spider):
    for data in item:
      if not data:
        raise DropItem("Missing data!")

    # answer
    if 'answer' in item:
      self.answers.update({'url': item['url']}, dict(item), upsert=True)
      log.msg("Added a documentation to answers!", level=log.DEBUG, spider=spider)
      return item
		  
    # question
    if 'question' in item:
      self.questions.update({'url': item['url']}, dict(item), upsert=True)
      log.msg("Added a documentation to questions!", level=log.DEBUG, spider=spider)
      return item