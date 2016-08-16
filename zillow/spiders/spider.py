# -*- coding: utf-8 -*-
import scrapy
import locale
import os
import re
import datetime

from scrapy import Request
try:
    from items import ZillowItem
except:
    from ..items import ZillowItem


class ZillowSpider(scrapy.Spider):
    name = "zillow"
    allowed_domains = ["zillow.com"]
    start_urls = ["http://www.zillow.com/homes/for_sale/Manhattan-New-York-NY-10001"]

    def parse(self, response):
        for listing in response.xpath(
                '//div[@id="search-results"]//ul[@class="photo-cards"]/li//a[contains(@href, "homedetails")]/@href'):
            listing = listing.extract()
            url = response.urljoin(listing.strip())
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        address = response.xpath('//header[@class="zsg-content-header addr"]/h1/text()').extract()

        if address:
            item = ZillowItem()

            itemprop_address = response.xpath('//span[@itemprop="address"]')
            street = response.xpath('//span[@itemprop="streetAddress"]/text()').extract()
            street = street[0].strip() if street else None
            city = response.xpath('//span[@itemprop="addressLocality"]/text()').extract()
            city = city[0].strip() if city else None
            state = response.xpath('//span[@itemprop="addressRegion"]/text()').extract()
            state = state[0].strip() if state else None
            zip_code = response.xpath('//span[@itemprop="postalCode"]/text()').extract()
            zip_code = zip_code[0].strip() if zip_code else None

            item['street'] = street
            item['city'] = city
            item['state'] = state
            item['zip_code'] = zip_code

            return item

        else:
            return None
