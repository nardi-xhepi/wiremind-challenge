import scrapy
import json

class TransaviaSpider(scrapy.Spider):
    name = 'transavia'

    start_urls = [
        'https://www.transavia.com/fr-FR/reservez-un-vol/vols/multidayavailability/',
        'https://www.transavia.com/fr-FR/reservez-un-vol/vols/SingleDayAvailability/'
    ]

    custom_settings = {
        "CONCURRENT_REQUESTS" : 1,
        "DEFAULT_REQUEST_HEADERS" : {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
        }
    }

    def __init__(self, origin, destination, departure_date, return_date, **kwargs):
        dep_date = [int(x) for x in departure_date.split("/")]
        ret_date = [int(x) for x in return_date.split("/")]

        self.origin = origin
        self.destination = destination


        self.body1 = f'selectPassengersCount.AdultCount=1&selectPassengersCount.ChildCount=0&selectPassengersCount.InfantCount=0&routeSelection.DepartureStation={origin}&routeSelection.ArrivalStation={destination}&dateSelection.OutboundDate.Day={dep_date[0]}&dateSelection.OutboundDate.Month={dep_date[1]}&dateSelection.OutboundDate.Year={dep_date[2]}&dateSelection.InboundDate.Day={ret_date[0]}&dateSelection.InboundDate.Month={ret_date[1]}&dateSelection.InboundDate.Year={ret_date[2]}&dateSelection.IsReturnFlight=true&flyingBlueSearch.FlyingBlueSearch=false'
        self.body2 = f'selectSingleDayAvailability.JourneyType=OutboundFlight&selectSingleDayAvailability.Date.DateToParse={dep_date[2]}-{dep_date[1]}-{dep_date[0]}&selectSingleDayAvailability.AutoSelect=false'
        self.body3 = f'selectSingleDayAvailability.JourneyType=InboundFlight&selectSingleDayAvailability.Date.DateToParse={ret_date[2]}-{ret_date[1]}-{ret_date[0]}&selectSingleDayAvailability.AutoSelect=false'



    def start_requests(self):

        cookies = {
            "reese84" : '3:X4u2QAfRgWd5OCb8X/YZtA==:3P4hRl9CgK4jNnrZ1ToG6KFo+UvsgZl11dzyWGZzY8B0wJSpSlU9W8R9CxW9rzs//hU4jtnhicMDBxIa3YZ+V40+hMtHz3POzsQHOQU+UcmNhKyU+SXCH0V6+AOVodMs+0TFtRwxzqLZeASElCKP5dRO6JCUTwoQaaFj5jwT3vDws5BYqujdn9P/McW9cR1CcoXlawVlv4gGewI9A9XZnVwtoFUQz4U4RHX0yn1hW31z9EaPF3mLrU3CXxegbzbzHKsBZgvhi59LuMk10nN+i5AdlF+HbvzohjBK08aHpaqnHkVhN1KBW4SJ48aFBaAGP9HUKBhxXKRS3qtKNJ3mma1aVgPDkSzsR3A4IRxnfog2Sr6Wq9CAIvTG2yAezMrk5yGOelywsju+awtKiwTqf7Vy0AnmVz5D090NbNweJRMBjoVJFAE+ojvOzCkGBR1IRjoAVQZsIf4N/MGN9MXBoBbRQqmWGMQJi8CczKVAQmCdlepEBl0Z9LDIZ0hqiA80:Sq5UQ0myIpUzqsKUUXnsfNICPaenLJKQZsxPZtT0Y1s=',
            #"ASP.NET_SessionId" : "itimyqvc0vvywzl5g3wxu3or"
        }

        yield scrapy.Request(self.start_urls[0], method='POST', body=self.body1, cookies=cookies)
        yield scrapy.Request(self.start_urls[1], method='POST', body=self.body2, cookies=cookies)
        yield scrapy.Request(self.start_urls[1], method='POST', body=self.body3, cookies=cookies)

    def parse(self, response):
        data = json.loads(response.body)
        if(response.url != self.start_urls[0]):
            if data["TagMan"]["eventData"]['day_view_search']['arrivalStation'] == self.destination:
                flights = data["TagMan"]["eventData"]['day_view_outbound_flights']
                single_day = "SingleDayOutbound"
            else:
                flights = data["TagMan"]["eventData"]['day_view_inbound_flights']
                single_day = "SingleDayInbound"

            for flight in flights:
                flight_number = flight['flight_label'] + flight['flight_number']
                origin = flight["departure"]
                destination = flight["arrival"]
                departure_time = flight['flight_time']

                date = flight['flight_date'].replace('-', '/')


                html = data[single_day]
                selector = scrapy.Selector(text=html)

                arrival_time = selector.xpath(f'//div[@class="times"][.//time[@class="departure"][starts-with(@datetime, "{date}")][normalize-space()="{departure_time}"]]/time/text()').getall()[1].replace(" ", "")

                cabinClass = flight['flight_class']
                price = flight['flight_cost'] + '€'


                yield {
                    "Flight Number" : flight_number,
                    'Origin' : origin,
                    'Destination' : destination,
                    'Departure time' : departure_time,
                    'Arrival time' : arrival_time,
                    'comfort title' : cabinClass,
                    'Price' : price
                }

