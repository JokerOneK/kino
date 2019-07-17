import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.kino.kz")
        # self.assertIn("Python", driver.title)

        elem = driver.find_element_by_xpath("//select[@name='name']")
        all_options = elem.find_element_by_tag_name("option")
        for option in all_options:
            print("Value is: %s" % option.get_attribute("value"))
            option.click()

        assert "No results found" not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
