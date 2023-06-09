#Scraping script for https://www.transavia.fr

import scrapy

class TransaviaSpider(scrapy.Spider):
    name = 'transavia'

    def start_requests(self):
        url = "https://www.transavia.com/fr-FR/reservez-un-vol/vols/rechercher/"
        yield scrapy.Request(url, meta={'playwright': True})

    def parse(self, response):
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

        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.parse_flights
        )

    def parse_flights(self, response):
        self.log('Form submitted, you can parse the response now')

