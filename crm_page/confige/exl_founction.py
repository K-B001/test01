import xlrd

class Crm_xlrd:
    def __init__(self,case_no,path,exlname):

        self.path=path
        self.case=xlrd.open_workbook(self.path)
        self.case_no=case_no
        self.exlname=exlname
    def get_user(self):

        user=self.case.sheet_by_index(self.exlname).cell_value(self.case_no,2)
        return user
    def get_url(self):
        url = self.case.sheet_by_index(self.exlname).cell_value(self.case_no, 1)
        return url
    def get_password(self):
        password = int(self.case.sheet_by_index(self.exlname).cell_value(self.case_no,3))
        return password
    def get_three(self):
        three = self.case.sheet_by_index(self.exlname).cell_value(self.case_no, 3)
        return three
    def get_four(self):
        four = int(self.case.sheet_by_index(self.exlname).cell_value(self.case_no, 4))
        return four


