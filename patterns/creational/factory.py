import logging
import os

logging.basicConfig(level=logging.INFO)


class LogTypeInterface(object):
    def write_log(self):
        pass


class FileHandlerLogType(LogTypeInterface):
    def write_log(self):
        logging.info('logging from FileHandlerLogType')


class StdOutLogType(LogTypeInterface):
    def write_log(self):
        logging.info('logging from StdOutLogType')


class LogTypeFactory(object):
    @staticmethod
    def create_log_instance() -> LogTypeInterface:
        if os.getenv('DEV') is not None:
            return StdOutLogType()
        else:
            return FileHandlerLogType()
