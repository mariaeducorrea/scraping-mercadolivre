import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"] #lista que contém a url onde o spider irá coletar os dados
    page_count = 1  #controla quantidade de páginas para processar
    max_pages = 10  #limita o número total de páginas a serem coletadas

    def parse(self, response):  #metodo parse chamado para processar a resposta da URL.
        products = response.css('div.ui-search-result__content')    #Seletor css para encontrar todos os elementos que contêm informações do produto

        
        for product in products:    #para cada produto encontrado, o código exrai informações específicas.

            prices = product.css('span.andes-money-amount__fraction::text').getall()
            cents = product.css('span.andes-money-amount__cents::text').getall()

            yield {
                'brand': product.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get(),
                'name': product.css('a.ui-search-link__title-card.ui-search-link::text').get(),
                'old_price_reais': prices[0] if len(prices) > 0 else None,
                'old_price_centavos': cents[0] if len(cents) > 0 else None,
                'new_price_reais': prices[1] if len(prices) > 1 else None,
                'new_price_centavos': cents[1] if len(cents) > 1 else None,
                'reviews_rating_number': product.css('span.ui-search-reviews__rating-number::text').get(),
                'reviews_amount': product.css('span.ui-search-reviews__amount::text').get()
            }

        if self.page_count < self.max_pages: #verifica se a contagem de páginas é menor que o número máximo
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()  #busca especificamente o atributo href do link da próxima página
            if next_page:   #verifica se next_page contém uma URL válida
                self.page_count += 1    #Se próxima página existir o contador é incrementado em 1
                yield scrapy.Request(url=next_page, callback=self.parse)    

                #scrapy.Request - nova requisição para a URL da próxima página
                #callback=self.parse -  resposta dessa nova requisição deve ser processada pelo mesmo método parse