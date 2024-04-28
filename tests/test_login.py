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
