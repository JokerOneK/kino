from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()

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


cells = []
tds = driver.find_elements_by_class_name("txt-rounded")
for td in tds:
    cells.append(td.get_attribute("innerHTML"))

# index = 0
# table = driver.find_element_by_class_name("schedule")
# rows = table.find_element_by_tag_name("tr")
# rows.ge


# print(cin)

cinemas = driver.find_elements_by_xpath("//*[@id='seances_8165']/tbody/tr/td[1]/a")
print([cinema.text for cinema in cinemas])

print(cells)
time.sleep(2)
driver.close()

