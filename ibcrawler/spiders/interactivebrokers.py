#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Interactive Brokers Crawling

Author: Svyatoslav Sydorenko
This spider uses POST requests to navigate search results.
It fetches four cells from each line and puts them into items.
"""

from bs4 import BeautifulSoup

from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import FormRequest

from ibcrawler.items import IbcrawlerItem


class IBSpider(CrawlSpider):
    """Spider for Interactive Brokers"""

    name = "Interactive Brokers Spider"
    allowed_domains = ["www1.interactivebrokers.ch", ]
    start_urls = ["http://www1.interactivebrokers.ch/" +
                  "contract_info/v3.8/index.php"]

    def parse_start_url(self, response):
        """Initial request"""

        # Submitting the search form to calculate pages count in callback
        return FormRequest.from_response(response, formname='refreshForm',
                                          formdata={
                                              'action': 'Advanced Search'
                                          },
                                          callback=self.navigate_tabs)

    def navigate_tabs(self, response):
        """Navigating results by submitting the search form"""

        soup = BeautifulSoup(response.body)
        items_count = int(soup.find('table', class_='resultsTbl')
                          .findAll('b')[2].string)
        tabs_count = items_count + (1 if items_count % 100 else 0)
        self.log('Tabs amount is {0}'.format(tabs_count))

        return [FormRequest.from_response(response, formname='refreshForm',
                                          formdata={
                                              'action': 'Advanced Search',
                                              'start': str(p)
                                          },
                                          callback=self.parse_page)
                for p in range(1, tabs_count + 1)]

    def parse_page(self, response):
        """Fetch table lines into items one by one"""

        soup = BeautifulSoup(response.body)

        for row in soup.find('table', class_='resultsTbl')\
                    .findChildren('tr', class_='odd', recursive=False):

            cells = row.findChildren('td', recursive=False)
            item = IbcrawlerItem()

            item['description'] = cells[1].find('b').string
            item['type'] = cells[2].string
            item['symbol'] = cells[3].string
            item['exchange'] = cells[4].string

            yield item
