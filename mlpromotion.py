import scrapy

# Define a spider class that inherits from Scrapy's Spider class
class MlpromotionSpider(scrapy.Spider):
    # Set the spider's name
    name = 'mlpromotion'
    # Define the URLs to start crawling from
    start_urls = ['https://www.mercadolivre.com.br/ofertas#nav-header']

    # Define the parsing method that will extract information from the HTML response
    def parse(self, response, **kwargs):
        # Initialize a counter variable to keep track of the index of the item being processed
        cont = 0
        # Loop through all elements in the HTML response that match the specified CSS selector
        for i in response.css('.promotion-item__description'):
            # Extract the price of the item
            price = i.css('.andes-money-amount--cents-superscript .andes-money-amount__fraction::text').get()
            # Extract the title of the item
            title = i.css('.promotion-item__title::text').get()
            # Extract the link to the item's page
            link = response.css('.items_container a::attr(href)')[cont].get()

            # Yield a dictionary with the extracted information
            yield {
                'price': price,
                'title': title,
                'link': link
            }
            # Increment the counter variable
            cont += 1

        # Extract the link to the next page of results
        prox_pag = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "andes-pagination__button--next", " " ))]//*[contains(concat( " ", @class, " " ), concat(" ", "andes-pagination__link", " " ))]').attrib['href']
        # If there is a next page, follow the link and call the parse method recursively
        if prox_pag is not None:
            yield response.follow(prox_pag, callback=self.parse)




