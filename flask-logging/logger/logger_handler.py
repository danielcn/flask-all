import os
import logging

log_name = 'myLogger'
logger = logging.getLogger(log_name)


class LoggerHandler:
    def __init__(self, level):
        logger.setLevel(level)

    def log_critical(self, message):
        return logger.critical(message)

    def log_error(self, message):
        return logger.error(message)

    def log_warning(self, message):
        return logger.warning(message)

    def log_info(self, message):
        return logger.info(message)

    def log_debug(self, message):
        return logger.debug(message)
