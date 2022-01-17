from scrapfly import ScrapeConfig, ScrapflyClient, ScrapeApiResponse
from bs4 import BeautifulSoup

scrapfly = ScrapflyClient(key='aec7da62495b44e1b030b6c331e982e9')
PAYLOAD = {'options': '[]', 'pid': '10937100030', 'quantity': '1'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}



api_response:ScrapeApiResponse = scrapfly.scrape(ScrapeConfig(
    url='https://www.snipesusa.com/on/demandware.store/Sites-snipesusa-Site/en_US/Cart-AddProduct',
    method='POST',
    data=PAYLOAD,
    asp=True
))

soup = BeautifulSoup(api_response.scrape_result['content'])
print(soup)