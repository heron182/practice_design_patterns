"""
http://web.archive.org/web/20120309135549/http://dpip.testingperspective.com/?p=28
*TL;DR80
Encapsulates how a set of objects interact.

https://sourcemaking.com/design_patterns/mediator/python/1

https://stackoverflow.com/questions/41266495/what-is-an-example-in-the-real-world-that-uses-the-mediator-pattern
"""
import time
import random


class TestClass(object):

  def __init__(self):
    self._tm = None
    self._bProblem = 0

  def setup(self):
    print("Setting up the Test")
    time.sleep(0.1)
    self._tm.prepareReporting()

  def execute(self):
    if not self._bProblem:
      print("Executing the test")
      time.sleep(0.1)
    else:
      print("Problem in setup. Test not executed.")

  def tearDown(self):
    if not self._bProblem:
      print("Tearing down")
      time.sleep(0.1)
      self._tm.publishReport()
    else:
      print("Test not executed. No tear down required.")

  def setTm(self, tm):
    self._tm = tm

  def setbProblem(self, bProblem):
    self._bProblem = bProblem


class Reporter(object):

  def __init__(self):
    self._tm = None

  def prepare(self):
    print("Reporter Class is preparing to report the results")
    time.sleep(0.1)

  def report(self):
    print("Reporting the results of Test")
    time.sleep(0.1)

  def setTm(self, tm):
    self._tm = tm


class DB:

  def __init__(self):
    self._tm = None

  def insert(self):
    print("Inserting the execution begin status in the Database")
    time.sleep(0.1)
    # Following code is to simulate a communication from DB to TC
    if random.randrange(1, 4) == 3:
      return -1

  def update(self):
    print("Updating the test results in Database")
    time.sleep(0.1)

  def setTm(self, tm):
    self._tm = tm


class TestManager(object):

  def __init__(self, testClass, reporter, db):
    self._testClass = testClass
    self._reporter = reporter
    self._db = db

  def prepareReporting(self):
    rvalue = self._db.insert()
    if rvalue == -1:
      self._testClass.setbProblem(1)
      self._reporter.prepareReporting()

  def publishReport(self):
    self._db.update()
    self._reporter.report()


def main():
  tc = TestClass()
  rp = Reporter()
  db = DB()

  tm = TestManager(tc, rp, db)

  tc.setTm(tm)
  rp.setTm(tm)
  db.setTm(tm)

  tc.setup()
  tc.tearDown()


if __name__ == '__main__':
  main()
