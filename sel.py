from selenium import webdriver
import time


def timetable_for_film(film):
    timetable_list = []
    times = driver.find_elements_by_xpath("//*[@id='%s']/tbody/tr/td[2]/div" % film)     # достать время фильма
    for time in times:
        timetable_list.append(time.get_attribute("innerHTML"))

    cinemas_list = []
    cinemas = driver.find_elements_by_xpath("//*[@id='%s']/tbody/tr/td[1]/a" % film)     # достать кино фильма
    for cinema in cinemas:
        cinemas_list.append(cinema.text)

    return list((zip(timetable_list, cinemas_list)))


def open_all():
    icons = driver.find_elements_by_class_name("mov_title_block")  # расркыть все фильмы
    for icon in icons:
        driver.execute_script("arguments[0].click();", icon)

    schedules = driver.find_elements_by_class_name("arr_select")  # раскрыть всё расписание
    for schedule in schedules:
        driver.execute_script("arguments[0].click();", schedule)

def get_name(film):
    name = driver.find_element_by_xpath("//a[@href='/movie/8286']")

driver = webdriver.Chrome()

driver.get("http://www.kino.kz")

open_all()

films_id_list = []
films_id = driver.find_elements_by_class_name("schedule")

for film_id in films_id[1:]:
    films_id_list.append(film_id.get_attribute("id"))


all_names_list = []

first_names = driver.find_elements_by_xpath("//*[@id='premiers-today']/div/ul/li/div/div[2]/dl/dt[2]/a")
for first_name in first_names:
    all_names_list.append(first_name.get_attribute("innerHTML"))

last_names = driver.find_elements_by_xpath("//*[@id='premiers-today']/div/div/div/div/div[2]/dl/dt[2]/a")
for last_name in last_names:
    all_names_list.append(last_name.get_attribute("innerHTML"))

print(all_names_list)


for film in films_id_list:
    print(timetable_for_film(film), "\n")


driver.close()

//*[@id='premiers-today']/div/ul/li[2]/div/div[2]/dl/dt[2]/a
//*[@id='premiers-today']/div/div/div[3]/div/div[2]/dl/dt[2]/a