import logging

import time

class AutoLog:
    def __init__(self):
        self.logger=logging.getLogger('log')
    def set_mes(self,mess,level_p):
        try:
            # 创建logger对象
            self.logger = logging.getLogger('log')

            now_dara = time.strftime('%Y-%m-%d', time.localtime())

            # 创建文件handle
            fh = logging.FileHandler('../log/auto' + now_dara + '.log')
            # 创建控制台handle
            ch = logging.StreamHandler()
            # 格式化
            fm = logging.Formatter('%(levelname)s %(asctime)s %(message)s')
            # 对文件格式
            fh.setFormatter(fm)
            # 对控制台格式
            ch.setFormatter(fm)
            # 文件句柄加入loger
            self.logger.addHandler(fh)
            # 控制台句柄加入logger
            self.logger.addHandler(ch)
            # 设置打印级别
            self.logger.setLevel(logging.INFO)
            # 输出info
            if level_p=='debug':
                self.logger.debug(mess)
            elif level_p=='info':
                self.logger.info(mess)
            self.logger.info('info message')
            # 移除文件句柄
            self.logger.removeHandler(fh)
            # 移除控制台对象
            self.logger.removeHandler(ch)
            # 关闭文件

        except:
            print('file exception')
        finally:
            fh.close()

