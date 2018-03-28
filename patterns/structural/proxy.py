"""
Provide a surrogate or placeholder for another object to control access
to it or add other responsibilities.
"""


class HeavyObjInterface(object):

  def expensive_computation(self):
    pass


class ConcreteHeavyObj(HeavyObjInterface):

  def expensive_computation(self):
    print('Making a heavy computation')


class HeavyObjProxy(HeavyObjInterface):
  _concreteObj = None

  def __init__(self):
    if not self._concreteObj:
      self._concreteObj = ConcreteHeavyObj()

  def expensive_computation(self):
    self._concreteObj.expensive_computation()


def main():
  proxy = HeavyObjProxy()
  proxy.expensive_computation()

  proxy2 = HeavyObjInterface()
  assert proxy2.expensive_computation() is proxy.expensive_computation()


if __name__ == '__main__':
  main()
