import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin
import numpy as np

options = Options()
options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
chrome = Service("chromedriver_104.exe")
driver = webdriver.Chrome(options=options, service=chrome)
driver.set_window_size(1024, 600)
driver.maximize_window()


def get_attribute_css(tag):
    try:
        att = driver.find_element(By.CSS_SELECTOR, tag).get_attribute("innerHTML")
    except:
        att = np.NaN

    return att


def get_attribute_xpath(tag):
    try:
        att = driver.find_element(By.XPATH, tag).get_attribute("innerHTML")
    except:
        att = np.NaN

    return att


dict_link = dict({
    'Sleman': 'https://www.olx.co.id/sleman-kab_g4000071/dijual-rumah-apartemen_c5158?filter=type_eq_rumah',
    'Yogya': 'https://www.olx.co.id/yogyakarta-kota_g4000072/dijual-rumah-apartemen_c5158?filter=type_eq_rumah',
    'Bantul': 'https://www.olx.co.id/bantul-kab_g4000068/dijual-rumah-apartemen_c5158?filter=type_eq_rumah',
    'Kulon': 'https://www.olx.co.id/kulon-progo-kab_g4000070/dijual-rumah-apartemen_c5158?filter=type_eq_rumah',
    'Kidul': 'https://www.olx.co.id/gunung-kidul-kab_g4000069/dijual-rumah-apartemen_c5158?filter=type_eq_rumah'})

area_list = ['Sleman', 'Yogya', 'Bantul', 'Kulon', 'Kidul']


# Call value using key
def get_value(keyx):
    for key, value in dict_link.items():
        if keyx == key:
            return value

    return "key doesn't exist"


attribute = []

for area in area_list:
    for i in range(1, 301):
        link = urljoin(get_value(area), f'?page={i}')
        driver.get(link)
        time.sleep(5)

        try:
            lists = driver.find_element(By.CLASS_NAME, 'rl3f9._3mXOU')
            maind = lists.find_elements(By.CLASS_NAME, 'EIR5N')
        except:
            break

        full_list = []

        for item in maind:
            link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
            full_list.append(link)

        for end in full_list:
            try:
                driver.get(end)
                time.sleep(3.5)
            except:
                pass

            title = get_attribute_css("span[data-aut-id='itemTitle']")
            price = get_attribute_css("span[data-aut-id='itemPrice']")
            land = get_attribute_css("span[data-aut-id='value_p_sqr_land']")
            build = get_attribute_css("span[data-aut-id='value_p_sqr_building']")
            bed = get_attribute_css("span[data-aut-id='value_p_bedroom']")
            bath = get_attribute_css("span[data-aut-id='value_p_bathroom']")
            floor = get_attribute_css("span[data-aut-id='value_p_floor']")
            cert = get_attribute_css("span[data-aut-id='value_p_certificate']")
            loc = get_attribute_xpath(
                '//*[@id="container"]/main/div/div/div/div[5]/div[1]/div/section/div/div[1]/div/span')

            to_list = {
                'title': title,
                'price': price,
                'land': land,
                'building': build,
                'bed': bed,
                'bath': bath,
                'floor': floor,
                'certificate': cert,
                'location': loc
            }
            print(to_list, 'page :', i)
            attribute.append(to_list)

attribute = pd.DataFrame(data=attribute)
attribute.to_csv('Output\Early_Data_Scraped-Raw.csv', index=False)
