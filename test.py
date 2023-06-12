import requests

url = "https://www.transavia.com/fr-FR/reservez-un-vol/vols/multidayavailability/"

payload = "selectPassengersCount.AdultCount=1&selectPassengersCount.ChildCount=0&selectPassengersCount.InfantCount=0&routeSelection.DepartureStation=ORY&routeSelection.ArrivalStation=FCO&dateSelection.OutboundDate.Day=1&dateSelection.OutboundDate.Month=7&dateSelection.OutboundDate.Year=2023&dateSelection.InboundDate.Day=15&dateSelection.InboundDate.Month=7&dateSelection.InboundDate.Year=2023&dateSelection.IsReturnFlight=true&flyingBlueSearch.FlyingBlueSearch=false"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'reese84=3:X4u2QAfRgWd5OCb8X/YZtA==:3P4hRl9CgK4jNnrZ1ToG6KFo+UvsgZl11dzyWGZzY8B0wJSpSlU9W8R9CxW9rzs//hU4jtnhicMDBxIa3YZ+V40+hMtHz3POzsQHOQU+UcmNhKyU+SXCH0V6+AOVodMs+0TFtRwxzqLZeASElCKP5dRO6JCUTwoQaaFj5jwT3vDws5BYqujdn9P/McW9cR1CcoXlawVlv4gGewI9A9XZnVwtoFUQz4U4RHX0yn1hW31z9EaPF3mLrU3CXxegbzbzHKsBZgvhi59LuMk10nN+i5AdlF+HbvzohjBK08aHpaqnHkVhN1KBW4SJ48aFBaAGP9HUKBhxXKRS3qtKNJ3mma1aVgPDkSzsR3A4IRxnfog2Sr6Wq9CAIvTG2yAezMrk5yGOelywsju+awtKiwTqf7Vy0AnmVz5D090NbNweJRMBjoVJFAE+ojvOzCkGBR1IRjoAVQZsIf4N/MGN9MXBoBbRQqmWGMQJi8CczKVAQmCdlepEBl0Z9LDIZ0hqiA80:Sq5UQ0myIpUzqsKUUXnsfNICPaenLJKQZsxPZtT0Y1s=; ; 3; incap_ses_156_2445686=gi7NCe5yQDLjN6IoTToqAgtahmQAAAAALi75QQOezjcl+dDOCLvENA==; nlbi_2445686=DPv+eWveJk4DJtThV7XfuAAAAABUOZjfRxLDUekCu+i7YVL2; visid_incap_2445686=TJUWAhv3Qf63bvkix8FsSV8+g2QAAAAAQkIPAAAAAAA47TRuA3iI2V7mUgZbV4qW; ASP.NET_SessionId=c15u01yhnsblf3nthfjmisf0; SC_ANALYTICS_GLOBAL_COOKIE=a3da8091cb9048ed8f82044875ee98de|False; __RequestVerificationToken=hYs0chGd2GGhEsrDS2ODIlEFfxwVuWuLPPEr0z6G23iI8qqSD88j81DvwoAf1FZvDAWevBBEq9doTG4zo0H844s4wsXEc6Er9UQrxHwc8-k1; sitelang=/fr-FR/; websitefr#lang=fr-FR'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
