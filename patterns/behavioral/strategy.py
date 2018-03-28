"""
Define a family of algorithms, encapsulate each one, and make them
interchangeable. Strategy lets the algorithm vary independently from
clients that use it.
"""

import abc


class Validator(metaclass=abc.ABCMeta):

  @abc.abstractclassmethod
  def validate(self):
    pass


class RGValidator(Validator):

  def validate(self):
    print('Validating RG')


class CPFValidator(Validator):

  def validate(self):
    print('Validating CPF')


class ValidatorFactory(object):

  def create_validator(self, id_length):
    if id_length > 15:
      return RGValidator()
    if id_length < 15:
      return CPFValidator()


def main():
  validatorFactory = ValidatorFactory()
  id = str(1233433)
  validator = validatorFactory.create_validator(len(id))
  validator.validate()


if __name__ == '__main__':
  main()
