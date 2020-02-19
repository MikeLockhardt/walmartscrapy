# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WalmartItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Description = scrapy.Field()
    SKU = scrapy.Field()
    Barcode = scrapy.Field()
    Brand = scrapy.Field()
    MSRP = scrapy.Field()
    Cost = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    # ListPrice = scrapy.Field()
    # SalePrice = scrapy.Field()
    # ImageURL = scrapy.Field()
    # ImageFile = scrapy.Field()
    # Quantity = scrapy.Field()
    # Depth = scrapy.Field()
    # Height = scrapy.Field()
    # Weight = scrapy.Field()
    # Width = scrapy.Field()
    # Catagory = scrapy.Field()
    # SpecialType = scrapy.Field()
    # shippingType = scrapy.Field()
    pass





            