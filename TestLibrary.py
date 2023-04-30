from selenium import webdriver

class TestLibrary:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_browser(self, url):
        self.driver.get(url)

    def click_button(self, locator):
        self.driver.find_element_by_xpath(locator).click()

    def enter_text(self, locator, text):
        self.driver.find_element_by_xpath(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.driver.find_element_by_xpath(locator).text

    def close_browser(self):
        self.driver.quit()