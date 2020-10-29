import time

import yaml

from crm_page.base.browser_operation import BrowerOperation
from crm_page.base.usebrowser import UseBrower
from crm_page.confige.exl_founction import Crm_xlrd
from crm_page.confige.log_crm import AutoLog


class LoginPage:
    def __init__(self):
        self.exl=Crm_xlrd(1,'../log/crm_case.xlsx',1)
        self.log=AutoLog()
        with open('../confige/test.yaml') as yaml_file:
            self.data=yaml.load(yaml_file,yaml.FullLoader)
        self.ub = UseBrower()
        self.bo = BrowerOperation(UseBrower.driver)
        self.bo.open_url(self.exl.get_url())
    def login(self):
        self.log.set_mes('登陆','info')
        self.bo.send_keys(self.data['LoginPage']['username'], self.exl.get_user())
        self.bo.send_keys(self.data['LoginPage']['password'], self.exl.get_password())
        self.bo.click_element(self.data['LoginPage']['submit'])
        self.log.set_mes('登陆成功','info')
    def test_text(self):
        self.bo.driver.switch_to_frame(self.data['LoginPage']['yanzen'])
        a=self.bo.driver.find_element_by_xpath(self.data['LoginPage']['yanzen1']).text
        self.log.set_mes('验证成功', 'info')
        return a
    def get_txt(self):
        pass

