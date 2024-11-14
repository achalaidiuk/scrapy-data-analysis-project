import scrapy

from autoria.colors import color_palette
from autoria.items import AutoriaItem
from autoria.utils import (
    extract_engine_info,
    extract_horsepower,
    extract_color,
    extract_fuel_type,
    extract_gearbox
)


class AutoriaSpider(scrapy.Spider):
    name = "auto_ria"
    allowed_domains = ["auto.ria.com"]
    start_urls = ["https://auto.ria.com"]

    color_palette = color_palette

    euro_to_usd = 1 / 44.80
    uah_to_usd = 1 / 42.00

    def __init__(self, last_page=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_page = int(last_page)

    def start_requests(self):
        base_url = "https://auto.ria.com/uk/legkovie/?page="
        headers = {"User-Agent": "Mozilla/5.0"}

        for i in range(1, self.last_page + 1):
            yield scrapy.Request(url=base_url + str(i), headers=headers,
                                 callback=self.parse)

    def parse(self, response):
        for href in response.css(
                "div.ticket-title a.address::attr(href)"
        ).getall():
            self.log("Found url: %s" % href)
            yield response.follow(href, self.parse_car_details)

    def parse_car_details(self, response):
        item = AutoriaItem()

        car_details = response.css("h3.auto-content_title::text").get().split()
        item["car"] = car_details[0]
        item["model"] = " ".join(car_details[1:-1])
        item["year"] = car_details[-1]

        price_text = response.css(".price_value strong::text").get()
        if price_text:
            price_numeric = "".join(filter(str.isdigit, price_text))
            if "€" in price_text:
                item["price"] = round(int(price_numeric) * self.euro_to_usd, 2)
            elif "грн" in price_text or "₴" in price_text:
                item["price"] = round(int(price_numeric) * self.uah_to_usd, 2)
            else:
                item["price"] = int(price_numeric)
        else:
            item["price"] = "Не вказано"

        mileage_text = response.css(
            "#details > dl > dd:nth-child(2) > span.argument::text"
        ).get()
        item["mileage"] = int(
            "".join(
                filter(str.isdigit, mileage_text)
            )
        ) * 1000 if mileage_text else "Не вказано"

        engine_text = response.css(
            "#details > dl > dd:nth-child(3) > span.argument::text"
        ).get()
        item["engine"] = extract_engine_info(engine_text)

        horsepower = response.css(
            "#details > dl > dd:nth-child(3) > span.argument::text"
        ).get()
        item["horsepower"] = extract_horsepower(horsepower)

        color_texts = [
            response.css(
                f"#details > dl > dd:nth-child({i}) > span.argument::text"
            ).get()
            for i in [6, 7, 8, 9]
        ]
        item["color"] = extract_color(color_texts)

        fuel_type_text = response.css(
            "#details dl dd:nth-child(3) span.argument"
        ).get()
        item['fuel_type'] = extract_fuel_type(fuel_type_text)

        gearbox_texts = [
            response.css(
                f"#details > dl > dd:nth-child({i}) > span.argument::text"
            ).get()
            for i in [4, 5, 6, 7]
        ]
        item["gearbox"] = extract_gearbox(gearbox_texts, fuel_type_text)

        self.log(f"Car data: {item}")
        return item
