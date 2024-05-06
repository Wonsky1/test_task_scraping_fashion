from scrapy.exporters import XmlItemExporter


class CustomXmlItemExporter(XmlItemExporter):
    def __init__(self, file, **kwargs):
        super().__init__(file, **kwargs)
        self.root_element = "channel"
