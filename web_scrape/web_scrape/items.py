# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AquariumScapeItem(scrapy.Item):
	user_name = scrapy.Field()
	rank = scrapy.Field()
	average_category_score = scrapy.Field()
	average_tank_score = scrapy.Field()
	num_ratings = scrapy.Field()
	fish_kept = scrapy.Field()
	plants_kept = scrapy.Field()
	comments = scrapy.Field()
	image_urls = scrapy.Field()
	image_name = scrapy.Field()
	images = scrapy.Field()
    


