from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

website = "https://www.goal.com/en"
path = "../assets/chromedriver"

options = Options()
options.page_load_strategy = 'eager'

service = Service(executable_path=path)

driver = webdriver.Chrome(service=service, options=options)

driver.get(website)