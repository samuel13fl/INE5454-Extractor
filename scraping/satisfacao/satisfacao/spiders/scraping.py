import scrapy
from scrapy.http import Request
import time
import re


class Scraping(scrapy.Spider):
    name = 'scraping'
    base_url = 'URL-DA-PESQUISA-INTERNA'
    page_number = 1

    """
    Filtros que podem ser usados (filterBy)
        6months
        currentMonth
        thisWeek
        all
    """

    # Definindo os parâmetros
    version = "all"
    filterBy = "all"
    query = ""

    custom_settings = {
        'CONCURRENT_REQUESTS': 100,
    }

    cookies = {
        "google-auth-session": "TOKEN-DE-AUTENTICACAO",
        "google-auth-session.sig": "TOKEN-DE-AUTENTICACAO",
    }

    def __init__(self, app=None, *args, **kwargs):
        super(Scraping, self).__init__(*args, **kwargs)
        self.app = app

    def start_requests(self):
        self.start_time = time.time()
        url = self.mount_url()
        yield Request(url, cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        table = response.css('table')
        headers = table.css('thead th::text').getall()
        rows = table.css('tbody tr')

        for row in rows:
            data = ['Pesquisa Interna']
            for cell in row.css('td'):
                cell_text = cell.css('::text').get()
                if cell_text is not None:
                    cell_text = cell_text.strip()
                    cell_text = re.sub(r'\n', '', cell_text)
                    cell_text = re.sub(r'\s+', ' ', cell_text)
                    data.append(cell_text)
                else:
                    data.append('')
            yield dict(zip(["Fonte"] + headers, data))

        if not rows:
            end_time = time.time()
            total_time = end_time - self.start_time
            hours = int(total_time // 3600)
            minutes = int((total_time % 3600) // 60)
            seconds = int(total_time % 60)
            print()
            print(f"Tempo de execução: {hours}h {minutes}m {seconds}s")
            print()
            return

        self.page_number += 1
        next_url = self.mount_url()
        yield Request(next_url, cookies=self.cookies, callback=self.parse)

    def mount_url(self):
        params = {
            "app": self.app,
            "version": self.version,
            "filterBy": self.filterBy,
            "page": self.page_number,
            "query": self.query
        }

        url = self.base_url + "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        return url