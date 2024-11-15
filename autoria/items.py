# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutoriaItem(scrapy.Item):
    car = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    price = scrapy.Field()
    mileage = scrapy.Field()
    engine = scrapy.Field()
    horsepower = scrapy.Field()
    color = scrapy.Field()
    fuel_type = scrapy.Field()
    gearbox = scrapy.Field()

