# Webscraping of Mercado Livre's Deals of the Day using Scrapy
This is an example of how to use Scrapy to collect all the Deals of the Day on Mercado Livre's website and save the data to a CSV file. The code was developed in Python and can be easily adapted for other web scraping tasks.

## Final Product
The objective of the code is to collect the information of the Deals of the Day on Mercado Livre's website, including product name, price, link to the product page, and seller rating. The data is saved to a CSV file, which can be easily imported into other data analysis tools.

## Tools Used
The code was developed in Python 3 and uses the Scrapy library for web scraping. To save the data to a CSV file, the Python csv library was used.

## Execution Process
To execute the code, follow these steps:

1.  Ensure that Python 3 is installed on your machine.

2.  Install Scrapy using the following command in the terminal:

```
pip install scrapy
```
3.  Clone the repository on your machine using the following command:
```
git clone https://github.com/your-username/webscraping-mercado-livre.git
```
4.  Navigate to the project folder and execute the following command in the terminal:

```
scrapy crawl ofertas -o ofertas.csv
```
This command will initiate the web scraping process and save the data to a CSV file named "ofertas.csv".

5.  Open the CSV file in a data analysis tool, such as Excel, to view and manipulate the collected data.

With this code, it is possible to collect Mercado Livre's Deals of the Day easily and efficiently, enabling data-driven analyses and decision-making.
