'''
Multiple instances sharing the same state
'''


class Borg(object):
  __shared_state = {}

  def __init__(self):
    self.__dict__ = self.__shared_state
    self.state = 'Initial state'


class AnotherBorg(Borg):
  pass


def main():
  b1 = Borg()
  b1.state = 'B1'

  b2 = Borg()
  b2.state = 'b2'

  print(f'{b1.state}')
  print(f'{b2.state}')

  b3 = AnotherBorg()
  print(f'{b3.state}')
  print(f'{b1.state}')
  print(f'{b2.state}')


if __name__ == '__main__':
  main()
