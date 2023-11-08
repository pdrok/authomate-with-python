from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
# path = "c:/chromedriver"
# I put the driver on the windows path
# https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/

# headless-mode
options = Options()
options.add_argument("--headless=new")
service = Service()
driver = webdriver.Chrome(service=service, options=options)

driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/span').text
    subtitle = container.find_element(by="xpath", value='./a/h3').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title': titles,
           'subtitle': subtitles,
           'link': links}
df_headlines = pd.DataFrame(
    my_dict
)

df_headlines.to_csv('headlines-headless.csv')

driver.quit()