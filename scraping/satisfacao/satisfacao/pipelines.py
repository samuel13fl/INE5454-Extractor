# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from scrapy import signals
class CsvPipeline(object):
    def __init__(self):
        self.file = None
        self.csvwriter = None
        self.headers_written = False

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signal=signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.file = open(f"../../{spider.name}_output.csv", 'w', newline='', encoding='utf-8')
        self.csvwriter = csv.writer(self.file)

    def spider_closed(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if not self.headers_written:
            self.csvwriter.writerow(item.keys())
            self.headers_written = True

        self.csvwriter.writerow(item.values())
        return item

