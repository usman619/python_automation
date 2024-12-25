from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium import webdriver

path = "../assets/geckodriver"

profile_path = "/home/usman619/snap/firefox/common/.mozilla/firefox/9wrnhh0g.Personal"
profile = FirefoxProfile(profile_path)

options = Options()
options.page_load_strategy = 'normal'
options.profile = profile
# options.add_argument("-headless")

service = Service(executable_path=path)
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.thesun.co.uk/sport/football/")
print(driver.title)
driver.quit()
