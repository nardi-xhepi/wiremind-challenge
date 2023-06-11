import scrapy
from scrapy_playwright.page import PageMethod
from playwright_stealth import stealth_sync
from urllib .parse import urlencode

API_KEY = 'c011c850258c1fba42cae4781de900bc'

def get_scraperapi_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url


class TransaviaSpider(scrapy.Spider):
    name = 'transavia'
    allowed_domains = ["www.transavia.com"]

    def start_requests(self):
        url = get_scraperapi_url("https://www.transavia.com/fr-FR/")
        yield scrapy.Request(url, meta=dict(
            playwright = True,
        ))

    def parse(self, response):
        print(response.body)






async def parse(response):
    page = response.meta["playwright_page"]
    await page.close()

    token = response.css('input[name="__RequestVerificationToken"]::attr(value)').get()

    print("TOKEN : ", token)

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
