from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import pandas as pd
import time
from datetime import datetime
import os
import sys

# for creating the result in the directory as the executable
application_path = os.path.dirname(sys.executable)

now = datetime.now()
date_month_year = now.strftime("%d%m%y") # formate DDMMYYYY

website = "https://www.thesun.co.uk/sport/football/"
path = "/home/usman619/Downloads/web_drivers/chromedriver-linux64/chromedriver"

# Testing headless-mode
options = Options()
options.add_argument("-headless")
options.headless = True
options.page_load_strategy = 'eager'

# For debugging 
# service_args = ["--verbose"]

service= Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.set_page_load_timeout(300)
    driver.implicitly_wait(15)

    driver.get(website)
    
    time.sleep(5)
    # //div[@class="teaser__copy-container"]/a/h3
    containers = WebDriverWait(driver,20).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@class="teaser__copy-container"]'))
        )
    # print(f"No of containers = {len(containers)}")

    titles = []
    subtitles = []
    links = []

    for container in containers:
        title = container.find_element(By.XPATH,value='./a/span').text
        subtitle = container.find_element(By.XPATH,value='./a/h3').text
        link = container.find_element(By.XPATH,value='./a').get_attribute("href")

        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)

    my_dict = {
        'titles':titles,
        'subtitles':subtitles,
        'links':links
    }

    df_headlines = pd.DataFrame(my_dict)

    file_name = f'headlines-{date_month_year}.csv'
    final_path = os.path.join(application_path,file_name)

    df_headlines.to_csv(final_path)
except Exception as e:
    print(f"A Error has occurred: {e}")
finally:
    driver.quit()