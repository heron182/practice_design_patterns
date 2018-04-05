class Prototype(object):

  value = 'default'

  def clone(self, **attr):
    obj = self.__class__()
    obj.__dict__.update(attr)
    return obj


class PrototypeDispatcher(object):

  def __init__(self):
    self._objects = {}

  def getObject(self, obj_name):
    print(f'Getting object {obj_name}')
    return self._objects[obj_name]

  def setObject(self, name, obj):
    self._objects[name] = obj

  def delObject(self, obj_name):
    del self._objects[obj_name]


def main():
  dispatcher = PrototypeDispatcher()
  prototype = Prototype()

  proto1 = prototype.clone(value='origin', category='Double')
  proto2 = prototype.clone(value='conn', is_valid=True)
  dispatcher.setObject('proto1', proto1)
  dispatcher.setObject('proto2', proto2)

  print(dispatcher.getObject('proto1').category)
  print(dispatcher.getObject('proto2').value)


if __name__ == '__main__':
  main()
