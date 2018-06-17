# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:15:25 2018

@author: apavlides
"""

# -*- coding: utf-8 -*-
from __future__ import absolute_import
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from web_scrape.items import AquariumScapeItem

class AquariumScapeSpider(CrawlSpider):
    # The name of the spider
    name = "aquarium_spider"

    # The domains that are allowed (links to other domains are skipped)
    allowed_domains = ["www.ratemyfishtank.com"]

    # The URLs to start with
    start_urls = ['https://www.ratemyfishtank.com/photos-planted-tanks/order/page/1']

    # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_items method
    rules = [
		Rule(LinkExtractor(allow=(r'com/users/.', ), 
		deny=(r'com/privacy', ), 
		 canonicalize=True, 
		 unique=True),
            follow=True,
            callback="parse_items")
    ]
        
    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    # Method for parsing items
    def parse_items(self, response):     
        
        items = []
        item = AquariumScapeItem()
   
        src = response.css('#index_photo img::attr(src)').extract_first()
        tank_img = response.urljoin(src)
        item['image_urls'] = [tank_img]
        item['image_name'] = ["name_test"]
        item['user_name'] = response.selector.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "reeftank_panel_top", " " ))]//span/text()').extract()
        item['rank'] = response.selector.css('.margin_b+ b::text').extract()
        item['average_category_score'] = response.selector.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "clear", " " )) and (((count(preceding-sibling::*) + 1) = 7) and parent::*)]//b/text()').extract()
        item['average_tank_score'] = response.selector.css('.clear:nth-child(5) b::text').extract()
        item['num_ratings'] = response.selector.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "clear", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)]//b/text()').extract()
        item['fish_kept'] = response.selector.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "spe-list2", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "right", " " ))]/text()').extract()
        item['plants_kept'] = response.selector.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "spe-list1", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "right", " " ))]/text()').extract()
        item['comments'] = response.selector.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "image_comment", " " ))]/text()').extract()
        # Return all the found items
        items.append(item)
        return items
        