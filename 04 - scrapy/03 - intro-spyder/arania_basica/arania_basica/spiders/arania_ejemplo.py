import scrapy

class IntroSpyder(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )

        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()

        precios = etiqueta_contenedora.css(
            'div.product_price > p.price_color::text'
        ).extract()

        imagenes = etiqueta_contenedora.css(
            'div.image_container > a > img::attr(src)'
        ).extract()

        en_stock = etiqueta_contenedora.css(
            'div.product_price > p.instock.availability::text'
        ).extract()

        estrellas = etiqueta_contenedora.css(
            'p.star-rating.Two > i'
        ).extract()

        print(imagenes)