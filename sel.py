import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_search_in_python_org(self):

        driver = self.driver
        driver.get("http://www.kino.kz")
        lis = []

        elem = driver.find_element_by_xpath("//select[@name='city-select']")
        all_options = elem.find_elements_by_tag_name("option")
        for option in all_options:
            lis.append(option.get_attribute("city-select"))
        print(lis)

        assert "No results found" not in driver.page_source
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
