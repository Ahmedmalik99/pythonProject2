import pandas as pd
import selenium
from selenium.webdriver.common.by import By
import time
from selenium import webdriver











# a = len(p_title)
# b = len(p_link)
# c = len(p_price)
#
# print(a)
# print(b)
# print(c)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
all_data = []

driver.get("https://www.ebay.com/")
time.sleep(10)

search_box = driver.find_element(By.ID, "gh-ac")
search_box.send_keys("computer")

search_btn = driver.find_element(By.ID, "gh-btn")
search_btn.click()

p_titles = driver.find_elements(By.CLASS_NAME, "s-item__title")
p_links = driver.find_elements(By.CLASS_NAME, "s-item__link")
p_prices = driver.find_elements(By.CLASS_NAME, "s-item__price")

for i in range(len(p_titles)):
    title = p_titles[i].text
    link = p_links[i].get_attribute("href")
    price = p_prices[i].text
    all_data.append([title, link, price])

for c in range(9):
    next_btn = driver.find_element(By.CLASS_NAME, "pagination__next")
    next_btn.click()
    time.sleep(5)
    p_titles = driver.find_elements(By.CLASS_NAME, "s-item__title")
    p_links = driver.find_elements(By.CLASS_NAME, "s-item__link")
    p_prices = driver.find_elements(By.CLASS_NAME, "s-item__price")

    for i in range(len(p_titles)):
        title = p_titles[i].text
        link = p_links[i].get_attribute("href")
        price = p_prices[i].text
        all_data.append([title, link, price])

print("Data scraped successfully!")

df = pd.DataFrame(all_data, columns=["Title", "Link", "Price"])

df.to_excel("ebay_data.xlsx", index=False)
print("Data has been saved to ebay_data.xlsx")

driver.quit()
