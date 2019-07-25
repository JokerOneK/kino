from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


def time_for_film(film):
    times = []
    cells = driver.find_elements_by_xpath("//*[@id='%s']/tbody/tr/td[2]/div" % film)     # достать время фильма
    for cell in cells:
        times.append(cell.get_attribute("innerHTML"))

    cin = []
    cinemas = driver.find_elements_by_xpath("//*[@id='%s']/tbody/tr/td[1]/a" % film)     # достать кино фильма
    # print([cinema.text for cinema in cinemas])
    for cine in cinemas:
        cin.append(cine.text)

    return list((zip(times, cin)))


driver = webdriver.Chrome()

driver.get("http://www.kino.kz")

icons = driver.find_elements_by_class_name("mov_title_block")       # расркыть все фильмы
for icon in icons:
    driver.execute_script("arguments[0].click();", icon)


schedules = driver.find_elements_by_class_name("arr_select")        # раскрыть всё расписание
for schedule in schedules:
    driver.execute_script("arguments[0].click();", schedule)

names = []
film_names = driver.find_elements_by_class_name("schedule")

for name in film_names[1:]:
    names.append(name.get_attribute("id"))


all_names = []
first_names = driver.find_elements_by_xpath("//*[@id='premiers-today']/div/ul/li/div/div[2]/dl/dt[2]/a")
for first_name in first_names:
    all_names.append(first_name.get_attribute("innerHTML"))

last_names = driver.find_elements_by_xpath("//*[@id='premiers-today']/div/div/div/div/div[2]/dl/dt[2]/a")
for get_name in last_names:
    all_names.append(get_name.get_attribute("innerHTML"))

print(all_names)

for film in names:
    print(film)
    print(time_for_film(film), "\n")


time.sleep(2)

driver.close()
