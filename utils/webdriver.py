from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller


class Webdriver:
    def __init__(self):
        chromedriver_autoinstaller.install()
        self.service = Service(executable_path='../utils/chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()

    def open_url(self, url):
        self.driver.get(url)
