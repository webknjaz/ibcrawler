Interactive Brokers Crawler
===========================
This spider fetches Advanced search results from www1.interactivebrokers.ch

How to run
===========================
First, clone this repo:
```sh
$ git clone https://github.com/webknjaz/ibcrawler.git
$ cd ibcrawler
```
Next, you may optionally set up a virtualenv:
```sh
$ virtualenv -p python2.7 env
$ source env/bin/activate
```
Then, install dependencies:
```sh
(env) $ pip install beautifulsoup4 scrapy
```
After that you may start crawler with
```sh
(env) $ scrapy crawl "Interactive Brokers Spider"
```
To produce CVS add `-o results.cvs -t cvs` arguments to above command.

Notes
===========================
Written by Svyatoslav Sydorenko in scope of [oDesk job]
(https://www.odesk.com/jobs/Teach-how-scrape-particular-page_~018c1c67167e293654)
