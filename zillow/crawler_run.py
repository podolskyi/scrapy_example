#!/usr/bin/python
# -*- coding: utf8 -*-
import time
import scrapy
import os
import logging
import datetime

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from spiders.spider import ZillowSpider

PATH = os.path.dirname(os.path.realpath(__file__))

logging.basicConfig(filename=PATH + '/crawl.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    configure_logging()
    runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(ZillowSpider)
        reactor.stop()

    crawl()
    reactor.run()


if __name__ == '__main__':
    main()
