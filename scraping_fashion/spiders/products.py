import re
import xml.etree.ElementTree as ET

import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.http import Response


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["www.farfetch.com"]
    start_urls = ["https://www.farfetch.com/ca/shopping/women/dresses-1/items.aspx"]

    scrapped_products = 0  # Comment this if you want to parse all products
    PRODUCTS_TO_BE_SCRAPPED = 120  # Comment this if you want to parse all products

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.channel = ET.Element("channel")


    def parse(self, response: Response, **kwargs):
        product_cards = response.css("li[data-testid='productCard']")
        for product_card in product_cards:
            information = product_card.css("div[data-testid='information']")
            price = product_card.css("div[data-component='PriceBrief'] p[data-component='Price']::text").get()
            if hasattr(self, 'scrapped_products'):
                self.scrapped_products += 1
            yield {
                "title": information.css("p[data-component='ProductCardBrandName']::text").get(),
                "description": information.css("p[data-component='ProductCardDescription']::text").get(),
                "price": re.sub(r'\$|,', '', price) + ".00 USD",
            }
            if hasattr(self, 'PRODUCTS_TO_BE_SCRAPPED'):
                if self.scrapped_products >= self.PRODUCTS_TO_BE_SCRAPPED:
                    raise CloseSpider(f"Stopping parsing because {self.PRODUCTS_TO_BE_SCRAPPED} have been scrapped")
