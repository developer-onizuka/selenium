from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

service = Service('./chromedriver')

browser = webdriver.Chrome(service=service, options=options)
browser.get("https://tenki.jp/week/")
elements = browser.find_elements(By.XPATH, '//span[@class="title"]')
for element in elements:
    print(element.text)
browser.quit()
