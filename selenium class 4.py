import pandas as pd
import selenium
from selenium.webdriver.common.by import By
import time

driver = selenium.webdriver.Chrome()
driver.get("https://crypto-fundraising.info/deal-flow/")
iall_data = []

for i in range(1,2):
    project_name_list = []
    projects_element = driver.find_elements(By.CLASS_NAME,"t-project-link")
    for project in projects_element:
        anchor = project.get_attribute('href')
        project_name_list.append(anchor)
    for url in project_name_list:
        driver.get(url)
        time.sleep(5)
        project_name = driver.find_element(By.CLASS_NAME, "singleproject-name-ticker")
        print(project_name.text)
        try:
          project_website = driver.find_elements(By.CLASS_NAME, "linkwithicon")
        except:
            continue
        social_links = []
        for x in project_website:
             a = x.get_attribute('href')
             social_links.append(a)
        # try:
        #   project_twitter = driver.find_elements(By.XPATH,"linkwithicon")
        # except:
        #     continue
        # for j in range(len(project_website)):
        #     for y in project_twitter:
        #         b = y.get_attribute('href')
        # try:
        #   project_telegram = driver.find_element(By.XPATH,"//*[@id='primary']/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div/a[2]").get_attribute('href')
        # except:
        #     continue
        # try:
        #   project_discord = driver.find_element(By.XPATH,"//*[@id='primary']/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div/a[3]").get_attribute('href')
        # except:
        #     continue
        # try:
        #   project_github = driver.find_element(By.XPATH,"//*[@id='primary']/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div/a[4]").get_attribute('href')
        # except:
        #     continue

        all_data = [project_name] + social_links
        print(all_data)
        iall_data.append(all_data)
    next_page_url = "https://crypto-fundraising.info/deal-flow/page/" + str(i)
    driver.get(next_page_url)




# df = pd.DataFrame(iall_data, columns=["Project Name", "Website", "Twitter", "Telegram", "Discord", "Github"])
# df.to_excel("CryptoData_data.xlsx", index=False)

# print("data has been saved to excel file")