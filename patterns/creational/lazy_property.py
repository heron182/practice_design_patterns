import functools


class lazy_property(object):

  def __init__(self, fn):
    self.fn = fn
    functools.update_wrapper(self, fn)

  def __get__(self, instance, cls):
    if instance is None:
      return self
    val = instance.__dict__.get(self.fn.__name__, None)
    if val is None:
      print('Computing expensive property')
      #   setattr(instance, self.fn.__name__, self.fn(instance))
      val = instance.__dict__[self.fn.__name__] = self.fn(instance)
    return val

  def __set__(self, instance, value):
    instance.__dict__[self.fn.__name__] = value


class MyObject(object):

  @lazy_property
  def expensive_property(self):
    print('This is very expensive')  # This will only print once
    return 10


def main():
  obj = MyObject()
  print(obj.expensive_property)
  print(obj.expensive_property)
  print(obj.expensive_property)
  print(obj.expensive_property)


if __name__ == '__main__':
  main()
