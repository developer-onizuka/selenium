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
places = browser.find_elements(By.XPATH, '//section/ul/li/a/p[@class="name"]')
#for place in places:
#    print(place.text)
#print(type(places))
#print(places[0].text)

temps = browser.find_elements(By.XPATH, '//section/ul/li/a/p/span[@class="high-temp"]')
#for temp in temps:
#    print(temp.text)

data = []
for i in range(len(places)):
    data.append((places[i].text, temps[i].text))

print(data)

browser.quit()
