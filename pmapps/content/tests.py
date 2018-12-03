from django.test import TestCase

import logging
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler
from logging import Formatter

# Create your tests here.
class TestLog(TestCase):
    def test_assert(self):
        # self.assertEqual(1, 2, '1 why equal 2?')
        self.assertIn(9, [1, 2,3,4], '9 why in [1, 3, 4]')

    def test_log(self):
        logger = logging.getLogger()

        fileHandler = TimedRotatingFileHandler('logs/content.log')
        fileHandler.setLevel(logging.INFO)  # NOTSET -> DEBUG -> INFO -> WARNING -> ERROR -> FATAL

        formatter = Formatter('%(asctime)s  %(levelname)s: %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')

        fileHandler.setFormatter(formatter)

        iohandler = StreamHandler()
        iohandler.setLevel(logging.DEBUG)

        logger.addHandler(fileHandler)
        logger.addHandler(iohandler)

        logger.setLevel(logging.DEBUG)

        logger.info('this is a test log python file!')
        logger.error('this is error msg for python file!')
        logger.debug('this is dubug msg !')   # this msg is hiddern!
        # logger.fatal()   # critical()