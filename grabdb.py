from selenium import webdriver
import sqlite3
import time


def timetable_for_film(film):
    timetable_list = []
    times = driver.find_elements_by_xpath("//*[@id='%s']/tbody/tr/td[2]/div" % film)     # ПОЛУЧЕНИЕ ВРЕМЕНИ ФИЛЬМА
    for time in times:
        timetable_list.append(time.get_attribute("innerHTML"))

    cinemas_list = []
    cinemas = driver.find_elements_by_xpath("//*[@id='%s']/tbody/tr/td[1]/a" % film)     # ПОЛУЧЕНИЕ КИНОТЕАТРА ФИЛЬМА
    for cinema in cinemas:
        cinemas_list.append(cinema.text)

    return tuple(zip(timetable_list, cinemas_list))


def open_all():
    icons = driver.find_elements_by_class_name("mov_title_block")  # раскрыть все фильмы
    for icon in icons:
        driver.execute_script("arguments[0].click();", icon)

    schedules = driver.find_elements_by_class_name("arr_select")  # раскрыть всё расписание
    for schedule in schedules:
        driver.execute_script("arguments[0].click();", schedule)


def tuple_union(films, timetable):
    result = [
        (k, *v)
        for k, r in zip(films, timetable)
        for v in r
    ]

    return result


options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2,          # ОТКЛЮЧЕНИЕ КАРТИНОК И ТД
                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                            'durable_storage': 2}}

options.add_experimental_option('prefs', prefs)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

while True:

    driver = webdriver.Chrome(options=options)
    driver.get("http://www.kino.kz")

    open_all()

    total_list = []

    all_names_list = []

# ПОЛУЕНИЕ ИМЕН ФИЛЬМОВ

    first_names = driver.find_elements_by_xpath("//*[@id='premiers-today']/div/ul/li/div/div[2]/dl/dt[2]/a")
    for first_name in first_names:
        all_names_list.append(first_name.get_attribute("innerHTML"))

    last_names = driver.find_elements_by_xpath("//*[@id='premiers-today']/div/div/div/div/div[2]/dl/dt[2]/a")
    for last_name in last_names:
        all_names_list.append(last_name.get_attribute("innerHTML"))

    all_names_tuple = tuple(all_names_list)

    films_id_list = []

# ПОЛУЧЕНИЕ id ФИЛЬМОВ

    films_id = driver.find_elements_by_class_name("schedule")

    for film_id in films_id[1:]:
        films_id_list.append(film_id.get_attribute("id"))

    timetables = []
    for film in films_id_list:
        timetables.append(timetable_for_film(film))

    result = tuple_union(all_names_tuple, timetables)
    driver.close()


    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM movies"
    cursor.execute(sql)

    if cursor.fetchall() != result:
        cursor.execute("DELETE FROM movies")
        cursor.executemany("INSERT INTO movies VALUES (?,?,?)", result)
        conn.commit()
    conn.close()

    time.sleep(300)
