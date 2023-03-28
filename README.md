# Webscrapping de ofertas do Mercado Livre usando Scrapy
Este projeto é um exemplo de como usar o framework Scrapy para fazer webscrapping de ofertas do dia no site do Mercado Livre e salvar os dados em um arquivo CSV.

## Requisitos
Antes de executar o código, certifique-se de ter o Scrapy instalado em sua máquina. Você pode instalar o Scrapy usando o seguinte comando:

'''pip install scrapy'''
## Como executar o código
1. Clone este repositório para sua máquina.

2. Navegue para a pasta do projeto.

3. Execute o seguinte comando no terminal:

"scrapy crawl ofertas -o ofertas.csv"

O Scrapy irá acessar o site do Mercado Livre e buscar todas as ofertas do dia. Os dados serão salvos no arquivo ofertas.csv.

## Entendendo o código
O código do webscrapping está contido no arquivo ofertas_spider.py.
 A classe OfertasSpider define como o Scrapy deve buscar os dados no site do Mercado Livre.

O método start_requests é chamado quando o Spider é iniciado e define qual página do site deve ser acessada para iniciar a busca.
O método parse é responsável por extrair os dados da página e retornar um objeto Python com as informações desejadas.
O comando "scrapy crawl ofertas -o ofertas.csv" é usado para executar o Spider e salvar os dados em um arquivo CSV.

## Conclusão
O Scrapy é uma ferramenta poderosa para fazer webscrapping de sites. Com ele, é possível coletar dados de maneira eficiente e automatizada. Este projeto é apenas um exemplo simples de como usar o Scrapy para coletar dados do Mercado Livre, mas as possibilidades são infinitas.
