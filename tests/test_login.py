from utils import config
from pages import login
import time
import unittest


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.login_page = login.LoginPage()

    def test_valid_login(self):
        self.login_page.open_url(config.baseUrl)
        self.login_page.login("standard_user", "secret_sauce")

        time.sleep(2)
        self.assertEqual("https://www.saucedemo.com/inventory.html", self.login_page.driver.current_url)

        self.login_page.close()

    def test_empty_username(self):
        self.login_page.open_url(config.baseUrl)
        self.login_page.login("", "secret_sauce")

        message_error = self.login_page.driver.find_element(self.login_page.By.XPATH, "//h3[@data-test='error']")

        self.assertTrue(message_error, "Epic sadface: Username is required")

        self.login_page.close()

