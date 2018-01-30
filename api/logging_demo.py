# encoding=utf-8
"""
3 forms of logging conf:
    1. file based config - logging.config.fileConfig
    2. dict based config (recommended) - logging.config.dictConfig
    3. coded config
"""
import logging
from logging.config import fileConfig
from logging.config import dictConfig
import yaml


class FileConfigLog:
    """
    file configured log
    """

    def __init__(self):
        fileConfig('conf/logging_fileconf.ini')
        self.logger = logging.getLogger('loggingDemo')

    def do_logging(self):
        self.logger.debug('debug message')
        self.logger.info('info message')
        self.logger.warn('warn message')
        self.logger.error('error message')
        self.logger.critical('critical message')


class DictConfigLog:
    """
    dict configured log
    """

    def __init__(self):
        with open("conf/logging_dictconf.yaml") as conf:
            dictConfig(yaml.load(conf))
        self.logger = logging.getLogger('dictLogger')

    def do_logging(self):
        self.logger.debug('debug message')
        self.logger.info('info message')
        self.logger.warn('warn message')
        self.logger.error('error message')
        self.logger.critical('critical message')


class CodeConfigLog:
    """
    code configured log
    """

    def __init__(self):
        self.logger = logging.getLogger('encodelog')
        self.logger.setLevel(logging.DEBUG)
        self.__init_console_log()
        self.__init_file_log()

    def do_logging(self):
        self.logger.debug('debug message')
        self.logger.info('info message')
        self.logger.warn('warn message')
        self.logger.error('error message')
        self.logger.critical('critical message')

    def get_logger(self):
        return self.logger

    def __init_console_log(self):
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def __init_file_log(self):
        fh = logging.FileHandler("log/encodelog.log", 'w')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)


if __name__ == "__main__":
    FileConfigLog().do_logging()
    CodeConfigLog().do_logging()
    DictConfigLog().do_logging()
