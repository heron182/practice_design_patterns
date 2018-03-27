from abc import ABCMeta, abstractmethod


class LogHandler(metaclass=ABCMeta):  # Product interface

  @abstractmethod
  def getHandler(self):
    pass


class StreamHandler(LogHandler):

  def getHandler(self):
    return 'STREAM'


class FileHandler(LogHandler):

  def getHandler(self):
    return 'FILE'


class LogFactory(metaclass=ABCMeta):  # Creator interface

  def __init__(self):
    self.handler = None
    self.createLog()

  @abstractmethod
  def createLog(self):
    pass

  @abstractmethod
  def setLogHandler(self):
    pass

  @abstractmethod
  def getLogHandler(self):
    pass


class LogProd(LogFactory):

  def createLog(self):
    self.setLogHandler()

  def setLogHandler(self):
    self.handler = FileHandler()

  def getLogHandler(self):
    return self.handler


class LogDev(LogFactory):

  def createLog(self):
    self.setLogHandler()

  def setLogHandler(self):
    self.handler = StreamHandler()

  def getLogHandler(self):
    return self.handler
