# -*- coding: utf-8 -*-
BOT_NAME = 'winter'

SPIDER_MODULES = ['winter.spiders']
NEWSPIDER_MODULE = 'winter.spiders'

ITEM_PIPELINES = ['winter.pipelines.MongoDBPipeline', ] 
 
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "winter"
MONGODB_COLLECTION_Q = "questions"
MONGODB_COLLECTION_A = "answers"

DOWNLOAD_DELAY = 1