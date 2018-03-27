'''
Template Method Pattern should be used when there is an algorithm with
many implementations. The algorithm is defined in a base class and implementation
is done in the base and subclasses

https://stackoverflow.com/questions/1553856/where-should-we-use-template-method-pattern?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
'''


class MakeMeal(object):

  def prepare(self):
    pass

  def cook(self):
    print('Put in the oven')

  def eat(self):
    pass


class MakePizza(MakeMeal):

  def prepare(self):
    print('Preparing pizza.')

  def eat(self):
    print('Eating pizza')


class MakePasta(MakeMeal):

  def prepare(self):
    print('Preparing pasta.')

  def cook(self):
    print('Boil in water for 20 minutes.')

  def eat(self):
    print('Eating pasta')


def main():
  makePizza = MakePizza()
  makePizza.prepare()
  makePizza.cook()
  makePizza.eat()

  makePasta = MakePasta()
  makePasta.prepare()
  makePasta.cook()
  makePasta.eat()


if __name__ == '__main__':
  main()
