import scrapy

class MlpromotionSpider(scrapy.Spider):
    name = 'mlpromotion'
    start_urls = ['https://www.mercadolivre.com.br/ofertas#nav-header']

    def parse(self, response, **kwargs):
        cont = 0
        for i in response.css('.promotion-item__description'):
            price = i.css('.andes-money-amount--cents-superscript .andes-money-amount__fraction::text').get()
            title = i.css('.promotion-item__title::text').get()
            link = response.css('.items_container a::attr(href)')[cont].get()


            yield {
                'price': price,
                'title': title,
                'link': link
            }
            cont+=1

        prox_pag = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "andes-pagination__button--next", " " ))]//*[contains(concat( " ", @class, " " ), concat(" ", "andes-pagination__link", " " ))]').attrib['href']
        if prox_pag is not None:
            yield response.follow(prox_pag, callback=self.parse)






