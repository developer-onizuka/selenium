from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

service = Service('./geckodriver')

browser = webdriver.Firefox(service=service, options=options)
browser.get("https://github.com/developer-onizuka")
browser.save_screenshot('screenshot.png')
browser.quit()
