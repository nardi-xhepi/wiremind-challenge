#Scraping script for https://www.transavia.fr

import scrapy
from scrapy_playwright.page import PageMethod

class TransaviaSpider(scrapy.Spider):
    name = 'transavia'

    def start_requests(self):
        url = "https://www.transavia.com/"
        yield scrapy.Request(url,
            meta=dict(
                playwright = True,
                playwright_include_page = True,
                playwright_page_methods =[PageMethod('wait_for_selector', 'div')],
            ))

    def parse(self, response):
        print(response.body)

async def parse(response):
    page = response.meta["playwright_page"]
    await page.close()

    token = response.css('input[name="__RequestVerificationToken"]::attr(value)').get()

    formdata = {
        '__RequestVerificationToken': token,
        'routeSelection.DepartureStation': 'ORY',
        'routeSelection.ArrivalStation': 'TIA',
        'dateSelection.OutboundDate.Day': '01',
        'dateSelection.OutboundDate.Month': '07',
        'dateSelection.OutboundDate.Year': '2023',
        'dateSelection.InboundDate.Day': '10',
        'dateSelection.InboundDate.Month': '07',
        'dateSelection.InboundDate.Year': '2023',
        'selectPassengersCount.AdultCount': '1',
        'selectPassengersCount.ChildCount': '0',
        'selectPassengersCount.InfantCount': '0',
    }