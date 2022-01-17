from traceback import print_tb
import selenium
from selenium import webdriver



def checkout(cookies):
    driver = webdriver.Chrome('C:\chrome\chromedriver.exe')
    driver.get('https://www.snipesusa.com/cart')
    for c in cookies :
        driver.add_cookie({'name': c.name, 'value': c.value, 'path': c.path})
    