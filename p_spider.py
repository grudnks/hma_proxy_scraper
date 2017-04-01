#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
import re

class ProxySpider(scrapy.Spider):
    name = 'proxy_spider'
    start_urls = ['http://proxylist.hidemyass.com']

    def parse(self, response):
        id = 0
        table_rows = response.css('.proxy-results tbody>tr')

        for row in table_rows:

            cls_none = row.css('td:nth-child(2)>span>style::text').re(r'\.(.*)\{display:none}')

            ip_row = row.xpath("td[2]").re(r'</style>(.*)')[0]
            port_row = row.xpath('td[3]//text()').extract()[0].lstrip()

            for s in cls_none:
                ip_row = re.sub(r'<span class="'+s+'">.*?</span>', '', ip_row)
            ip_row = re.sub(r'<span style="display:none">.*?</span>', '', ip_row)
            ip_row = re.sub(r'<div style="display:none">.*?</div>', '', ip_row)
            ip_row = re.sub(r'</?span(.*?)>', '', ip_row)

            yield {'ip': ip_row.replace(' ',''),
                   'port': port_row.replace(' ','') }

            id += 1

    # scrapy runspider p_spider.py -o proxies.json