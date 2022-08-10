import logging

from common import mylog
from common import run_case

if __name__ == '__main__':
    mylog.configLog()
    logger = logging.getLogger('logger')
    logger.info('========开始测试========\n')
    run_case.run()
    logger.info('========结束测试========\n')
