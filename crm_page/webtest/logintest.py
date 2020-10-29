import time
import unittest
import sys
sys.path.append('E:\\PycharmProjects\\pythonProject')

from HTMLTestRunner import HTMLTestRunner
from crm_page.base.usebrowser import UseBrower
from crm_page.webpage.add_customer import AddCustomer
from crm_page.webpage.login_page import LoginPage


class Logintest(unittest.TestCase):
    def setUp(self) -> None:
        self.login=LoginPage()
        self.login.login()
        self.addcustomer = AddCustomer()

    def test_login(self):
        self.assertEqual(self.login.test_text(),'当前用户：张三')
    def test_add_customer(self):
        self.addcustomer.add_cu()


    def tearDown(self) -> None:
        UseBrower.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(Logintest)
    suite.addTest(test_case)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    # 创建HTML报告
    with open('../report/repot_' + date_now + '.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description='ui_auto_test')
        runner.run(suite)
