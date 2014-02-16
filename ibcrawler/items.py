# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class IbcrawlerItem(Item):
    """
    IbcrawlerItem - separate table item

    This class represents a single line
    crawled from table
    """
    description = Field()
    type = Field()
    symbol = Field()
    exchange = Field()
