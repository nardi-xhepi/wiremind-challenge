# Flight Data Scraping Spiders Documentation

This repository contains two Scrapy spiders, `ExpediaSpider` and `TransaviaSpider`, used to scrape flight data from different websites. Both spiders provide the following flight details: flight number, origin, destination, departure time, arrival time, class, and price.

## Common Requirements
- Python 3.7+
- Scrapy (Install with `pip install scrapy`)

## Usage

### ExpediaSpider

The `ExpediaSpider` is used to scrape flight data from Expedia.fr.

#### Usage Example:
```bash
scrapy crawl expedia -a origin="Paris" -a destination="Munich" -a departure_date="01/07/2023" -a return_date="15/07/2023" -O expedia.json
```

This command will start the `ExpediaSpider` to scrape flight information between Paris and Munich, departing on July 1, 2023, and returning on July 15, 2023.

Please note that the date must be formatted as `"DD/MM/YYYY"`.

### TransaviaSpider

The `TransaviaSpider` is used to scrape flight data from transavia.com.

#### Usage Example:
```bash
scrapy crawl transavia -a origin="ORY" -a destination="FCO" -a departure_date="01/07/2023" -a return_date="15/07/2023" -O transavia.json
```

This command will start the `TransaviaSpider` to scrape flight information between Paris and Rome, departing on July 1, 2023, and returning on July 15, 2023.

Please note that the date must be formatted as `"DD/MM/YYYY"`. Additionally, you need to input airport identifiers provided by Transavia for each airport. Unfortunately, it is not possible to directly use the city name as the destination.

## Output

Both spiders will return a list of available flights with the following details: flight number, origin, destination, departure time, arrival time, class, and price.

## Notes

Both scripts utilize the API call content found on the respective websites (Expedia.fr for `ExpediaSpider` and transavia.com for `TransaviaSpider`).