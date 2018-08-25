# Python Api Structure Template

## Overview

Many people ask me what is the best python structure to work, and I always say, what you fell more confortable to work with it :)

However I believe using module style is the best approuch,...
So lets create a new project using sanic calls: dercypy. this api will be a database for the best quotes from Dercy Gonçalves.

## requirements

- Docker (Docker version 18.03.1-ce)
- Python3.6
- Sanic
- Postgresql
- asyncpg
- scrapy
- docker-compose
- pytest-cov
- pytest

## structure

   


## scrapy - generate quotes

Lets going to use a awesome web crawling framework, scrapy.
This framework will help us to generate the Dercy's quotes data.

```python
import scrapy


class DercySpider(scrapy.Spider):
    name = "dercy"

    def start_requests(self):
        urls = ["https://kdfrases.com/autor/dercy-gon%C3%A7alves"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {"text": quote.css("a.qlink::text").extract_first()}

        next_pages = response.css("div a.page::attr(href)").extract()

        for next_page in next_pages:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


```

Execute the script

```bash
scrapy runspider dercypy/services/dercy.py -o static/dercy.json
```

## Docker image

Cleanup docker if needed. It will remove all containers/images/... from your docker so be careful

```bash
sudo docker system prune -a
```

Build it

```bash
sudo docker build -t dercy -f ./docker/Dockerfile .
```

Run it

```bash
sudo docker run --name dercy -t -d dercy
sudo docker exec -it dercy /bin/bash
```

Now that our container is running, lets create a docker-compose file to include database too

```bash
sudo docker-compose -f docker/docker-compose.yml up
```

for more information: [docker-compose-docs](https://docs.docker.com/compose/compose-file/#compose-and-docker-compatibility-matrix)