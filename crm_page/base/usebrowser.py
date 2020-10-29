import time

from selenium import webdriver


class UseBrower:
    driver=None
    def __init__(self):
        self.driver=webdriver.Chrome('../chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        UseBrower.driver=self.driver



    @classmethod
    def quit(cls):
        UseBrower.driver.quit()