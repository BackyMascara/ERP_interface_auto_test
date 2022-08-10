import os
import time
import logging

"""创建日志文件"""
def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass

"""配置日志器的路径、内容格式"""
def configLog():
    # 创建一个日志
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 把日志输入到log目录中
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path + '/log/all_log.log'
    err_file = path + '/log/error_log.log'
    create_file(log_file)
    create_file(err_file)

    # 创建一个handler，用于写入日志文件
    handler = logging.FileHandler(log_file, encoding='utf-8')
    err_handler = logging.FileHandler(err_file, encoding='utf-8')
    err_handler.setLevel(logging.ERROR)

    formator = logging.Formatter(fmt="%(asctime)s - [%(filename)s -->line:%(lineno)d] - %(levelname)s: %(message)s",
                                 datefmt="%Y/%m/%d/%X")
    handler.setFormatter(formator)
    err_handler.setFormatter(formator)

    logger.addHandler(handler)
    logger.addHandler(err_handler)

if __name__ == "__main__":
    configLog() # 配置日志器后，才能写入日志文件中
    logger = logging.getLogger('logger')
    logger.info('hahhaha')


