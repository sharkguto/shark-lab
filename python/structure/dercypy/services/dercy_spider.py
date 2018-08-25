import scrapy


class DercySpider(scrapy.Spider):
    name = "dercy"

    def start_requests(self):
        urls = ["https://kdfrases.com/autor/dercy-gon%C3%A7alves"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {"text": quote.css("a.qlink::text").extract_first()}

        next_pages = response.css("div a.page::attr(href)").extract()

        for next_page in next_pages:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
