# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecruitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    descrip = scrapy.Field()
    loc = scrapy.Field()
    job_type = scrapy.Field()
    url = scrapy.Field()


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    articleContent = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
