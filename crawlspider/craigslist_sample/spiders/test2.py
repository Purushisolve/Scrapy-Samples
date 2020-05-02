import scrapy 

from scrapy.selector import HtmlXPathSelector

from scrapy.spiders.crawl import Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor



class MySpider(CrawlSpider):
    name = "craigs"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath('//span[@class="pl"]')
        items = []
        for title in titles:
            item = items.CraigslistSampleItem()
            item["title"] = title.select('a/span[@id="titletextonly"]/text()').extract()
            item["link"] = title.xpath("a/@href").extract()
            items.append(item)
        return(items)
