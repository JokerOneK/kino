import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Safari()

driver.get("http://www.kino.kz")

# cities = []     # все города
# elem = driver.find_element_by_xpath("//select[@name='city-select']")
# all_options = elem.find_elements_by_tag_name("option")
# for option in all_options:
#     cities.append(option.get_attribute("innerHTML"))
# print(cities)

icons = driver.find_elements_by_class_name("mov_title_block")       # расркыть все фильмы
for icon in icons:
    driver.execute_script("arguments[0].click();", icon)

schedules = driver.find_elements_by_class_name("arr_select")        # раскрыть всё расписание
for schedule in schedules:
    driver.execute_script("arguments[0].click();", schedule)

time.sleep(2)
driver.close()
