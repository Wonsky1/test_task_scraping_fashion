import scrapy
from scrapy.http import Response


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["www.farfetch.com"]
    start_urls = ["https://www.farfetch.com/ca/shopping/women/dresses-1/items.aspx"]

    def parse(self, response: Response, **kwargs):
        product_cards = response.css("li[data-testid='productCard']").getall()
        for product_card in product_cards:
            pass
