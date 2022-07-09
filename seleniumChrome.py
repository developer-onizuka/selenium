from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

service = Service('./chromedriver')

browser = webdriver.Chrome(service=service, options=options)
browser.get("https://github.com/developer-onizuka")
browser.save_screenshot('screenshot.png')
browser.quit()
