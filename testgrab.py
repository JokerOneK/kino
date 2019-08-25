from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def open_all():
    icons = driver.find_elements_by_class_name("mov_title_block")  # раскрыть все фильмы
    for icon in icons:
        driver.execute_script("arguments[0].click();", icon)

    schedules = driver.find_elements_by_class_name("arr_select")  # раскрыть всё расписание
    for schedule in schedules:
        driver.execute_script("arguments[0].click();", schedule)



options = webdriver.ChromeOptions()
# prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2,          # ОТКЛЮЧЕНИЕ КАРТИНОК И ТД
#                             'plugins': 2, 'popups': 2, 'geolocation': 2,
#                             'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
#                             'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
#                             'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
#                             'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
#                             'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
#                             'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
#                             'durable_storage': 2}}
#
# options.add_experimental_option('prefs', prefs)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=options)

driver.get("http://www.kino.kz")
open_all()

city = driver.find_element_by_xpath("//*[@id='city-select-index-button']/span[1]")
city.click()

options = driver.find_elements_by_class_name("ui-menu-item")

option = driver.find_element_by_xpath('//*[@id="ui-id-11"]')
option.click()

# for i in options:
#     i.send_keys(Keys.COMMAND + "t")


time.sleep(5)
print("hello")

driver.close()
