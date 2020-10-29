



class BrowerOperation:
    def __init__(self,driver):
        self.driver=driver


    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url error')
    def send_keys(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'element not found')
    def click_element(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e,'element not found')


    def get_text(self,xpath):
        try:

            a=self.driver.find_element_by_xpath(xpath).text
            return a
        except Exception as e:
            print(e,'not found')
