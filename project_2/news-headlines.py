import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
# path = "../assets/chromedriver"
path = "../assets/chromedriver"
# path = "/home/usman619/snap/firefox/5437/usr/lib/firefox/geckodriver"
# Adding the path of firefox profile 
# profile_path = "/home/usman619/snap/firefox/common/.mozilla/firefox/zv6n1u4l.selenium-profile"
# profile = FirefoxProfile(profile_path)
# Adding Headers
# caps = DesiredCapabilities().CHROME
# caps["goog:loggingPrefs"] = {"performance": "ALL"}
# caps["chrome.page.customHeaders"] = {
#     "Accept-Language": "en-US,en;q=0.9",
#     "Referer": "https://www.google.com",
# }

# Testing headless-mode
options = Options()
options.add_argument("-headless")
options.headless = True
options.page_load_strategy = 'eager'

# options.add_argument("-profile")
# options.profile = profile
# options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/92.0")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

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
    print(f"No of containers = {len(containers)}")
    # print(containers)
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
    df_headlines.to_csv('headlines-headless.csv')
except Exception as e:
    print(f"A Error has occurred: {e}")
finally:
    driver.quit()