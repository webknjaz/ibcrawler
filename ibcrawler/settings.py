# Scrapy settings for ibcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ibcrawler'

SPIDER_MODULES = ['ibcrawler.spiders']
NEWSPIDER_MODULE = 'ibcrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ibcrawler (+http://www.yourdomain.com)'

DOWNLOAD_DELAY = 0.15  # 150 ms of delay
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_REQUESTS = 50
CONCURRENT_REQUESTS_PER_DOMAIN = 10
RETRY_TIMES = 2
