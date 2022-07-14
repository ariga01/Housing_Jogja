import time
import pandas as pd
from bs4 import BeautifulSoup
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


def get_values(css_tag="BLANK", class_tag="BLANK", xpath_tag="BLANK"):
    css_s = bool(css_tag)
    class_s = bool(class_tag)
    xpath_s = bool(xpath_tag)

    att = np.NaN

    if css_s != "BLANK":
        try:
            att = driver.find_element(By.CSS_SELECTOR, css_tag).get_attribute("innerHTML")
        except:
            att = np.NaN

    if pd.isna(att) is True and class_s != "BLANK":
        try:
            attribute_data = driver.find_element(By.CLASS_NAME, class_tag)
            att = BeautifulSoup(attribute_data.get_attribute('outerHTML'), 'html.parser').text
        except:
            att = np.NaN

    if pd.isna(att) is True and xpath_s != "BLANK":
        try:
            att = driver.find_element(By.XPATH, xpath_tag).get_attribute("innerHTML")
        except:
            att = np.NaN

    return att


dict_link = dict({
    'Sleman': 'https://www.olx.co.id/sleman-kab_g4000071/dijual-rumah-apartemen_c5158?filter=price_min_60000000%2Ctype_eq_rumah',
    'Yogya': 'https://www.olx.co.id/yogyakarta-kota_g4000072/dijual-rumah-apartemen_c5158?filter=price_min_60000000%2Ctype_eq_rumah',
    'Bantul': 'https://www.olx.co.id/bantul-kab_g4000068/dijual-rumah-apartemen_c5158?filter=price_min_60000000%2Ctype_eq_rumah',
    'Kulon': 'https://www.olx.co.id/kulon-progo-kab_g4000070/dijual-rumah-apartemen_c5158?filter=price_min_60000000%2Ctype_eq_rumah',
    'Kidul': 'https://www.olx.co.id/gunung-kidul-kab_g4000069/dijual-rumah-apartemen_c5158?filter=price_min_60000000%2Ctype_eq_rumah'})

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

        for webpage in full_list:
            try:
                driver.get(webpage)
                time.sleep(3.5)
            except:
                pass

            title = get_values(
                css_tag="span[data-aut-id='itemTitle']",
                xpath_tag='//*[@id="container"]/main/div/div/div/div[5]/div[1]/div/section/h1'
                )
            price = get_values(
                css_tag="span[data-aut-id='itemPrice']",
                xpath_tag='//*[@id="container"]/main/div/div/div/div[5]/div[1]/div/section/span[1]'
                )
            types = get_values(
                css_tag="span[data-aut-id='value_type']",
                xpath_tag='//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[1]/div/span[2]'
            )
            land = get_values(
                css_tag="span[data-aut-id='value_p_sqr_land']",
                xpath_tag='//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[3]/div/span[2]'
                )
            build = get_values(
                css_tag="span[data-aut-id='value_p_sqr_buildin']",
                xpath_tag='//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[2]/div/span[2]'
                )
            bed = get_values(
                css_tag="span[data-aut-id='value_p_bedroom']",
                xpath_tag='//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[4]/div/span[2]'
                )
            bath = get_values(
                css_tag="span[data-aut-id='value_p_bathroom']",
                xpath_tag='//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[5]/div/span[2]'
                )
            floor = get_values(
                css_tag="span[data-aut-id='value_p_floor']",
                xpath_tag='//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[6]/div/span[2]'
                )
            cert = get_values(
                css_tag="span[data-aut-id='value_p_certificate']",
                xpath_tag='//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[8]/div/span[2]'
                )
            loc = get_values(
                xpath_tag='//*[@id="container"]/main/div/div/div/div[5]/div[1]/div/section/div/div[1]/div/span')
            s_loc = get_values(
                css_tag="span[data-aut-id='value_p_alamat']",
                xpath_tag='//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[9]/div/span[2]'
            )

            to_list = {
                'title': title,
                'price': price,
                'types': types,
                'land': land,
                'building': build,
                'bed': bed,
                'bath': bath,
                'floor': floor,
                'certificate': cert,
                'location': loc,
                'secondary_location': s_loc,
                'url': webpage
            }
            print(to_list, 'page :', i)
            attribute.append(to_list)

attribute = pd.DataFrame(data=attribute)
attribute.to_csv('Output\Early_Data_Scraped-Raw.csv', index=False)
