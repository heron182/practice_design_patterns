"""
Convert the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of
incompatible interfaces.
"""


class Adapter(object):

  def __init__(self, adaptee):
    self.adaptee = adaptee

  def doSomethingNew(self, x, y):
    print('Tunneling to the old interface...')
    self.adaptee.doSomething()

  def __getattr__(self, name):
    return getattr(self.adaptee, name)


class Adaptee(object):

  def doSomething(self):
    print('Doing something')


def main():
  client = Adapter(Adaptee())
  client.doSomethingNew(1, 2)


if __name__ == '__main__':
  main()
