# coding=utf-8

import logging

LEVEL_DEBUG = logging.DEBUG
LEVEL_INFO = logging.INFO
LEVEL_ERROR = logging.ERROR

DEFAULT_FORMAT = "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
MESSAGE_FORMAT = "%(message)s"
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

MODE_APPEND = "a"
MODE_WRITE = "w"


def setup_logger(name, log_file, level=logging.INFO, fmt=DEFAULT_FORMAT, datefmt=DEFAULT_DATE_FORMAT, mode=MODE_APPEND):
    handler = logging.FileHandler(filename=log_file, mode=mode)
    handler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


def enable_stdout(level=logging.INFO, fmt=DEFAULT_FORMAT):
    console = logging.StreamHandler()
    console.setLevel(level)
    formatter = logging.Formatter(fmt)
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)


if __name__ == "__main__":
    enable_stdout(LEVEL_DEBUG)
    debug_logger = setup_logger("log_test_debug", "./log_test_debug.log", LEVEL_DEBUG, mode=MODE_WRITE)
    info_logger = setup_logger("log_test_info", "./log_test_info.log", LEVEL_INFO, mode=MODE_WRITE)
    err_logger = setup_logger("log_test_error", "./log_test_error.log", LEVEL_ERROR, mode=MODE_WRITE)

    for i in range(0, 10):
        debug_logger.debug("debug %s", i)
        info_logger.info("info %s", i)
        err_logger.error("error %s", i)