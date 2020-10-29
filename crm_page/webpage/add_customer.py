import time

import yaml

from crm_page.base.browser_operation import BrowerOperation
from crm_page.base.usebrowser import UseBrower
from crm_page.confige.exl_founction import Crm_xlrd
from crm_page.webpage.login_page import LoginPage


class AddCustomer:

    def __init__(self):
        self.exl = Crm_xlrd(1,'../log/crm_case.xlsx',2)
        with open('../confige/test.yaml') as yaml_file:
            self.data=yaml.load(yaml_file,yaml.FullLoader)
        self.loginn = LoginPage()




    def add_cu(self):
        self.loginn.login()
        time.sleep(5)
        self.loginn.bo.driver.switch_to.frame(self.data['LoginPage']['yanzen'])
        self.loginn.bo.click_element(self.data['AddCustomer']['customer_new'])
        self.loginn.bo.driver.switch_to.parent_frame()
        self.loginn.bo.driver.switch_to.frame(self.data['AddCustomer']['customr_frame_name'])

        self.loginn.bo.click_element(self.data['AddCustomer']['customer_add'])
        self.loginn.bo.send_keys(self.data['AddCustomer']['username'],self.exl.get_user())
        self.loginn.bo.send_keys(self.data['AddCustomer']['userjob'],self.exl.get_three())
        self.loginn.bo.send_keys(self.data['AddCustomer']['email'],self.exl.get_four)
