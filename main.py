import json
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from checkout import checkout




sesssion = requests.session

URL = 'https://www.snipesusa.com/on/demandware.store/Sites-snipesusa-Site/en_US/Product-Variation?dwvar_1000096042_color=H01315&dwvar_1000096042_size=9&pid=1000096042&quantity=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Accept-Language': 'en,en-US;q=0,5',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8'

    }
params = {
    "dwvar_1000096042_color": 'H01315',
    "dwvar_1000096042_size": "9",
    "pid": "1000096042",
    "qauntity": "1"
}
 

r = requests.get(URL, headers=headers)
data = r.json
pid_for_size = data()['product']['id']

ADD_TO_CART_URL = 'https://www.snipesusa.com/on/demandware.store/Sites-snipesusa-Site/en_US/Cart-AddProduct'
PAYLOAD = {'options': '[]', 'pid': pid_for_size, 'quantity': '1'}

p = requests.post(ADD_TO_CART_URL, data = PAYLOAD, headers=headers)

s = Service('C:\chrome\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.snipesusa.com/cart')
checkout(p.cookies)



