from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

service = Service('./chromedriver')

browser = webdriver.Chrome(service=service, options=options)
browser.get("https://github.com/developer-onizuka")
elements = browser.find_elements(By.XPATH, '//a[@href]')
#elements = browser.find_elements(By.XPATH, '//a[@href][1]')
for element in elements:
    print(element.get_attribute("href"))
    #print(element.text)
browser.quit()
