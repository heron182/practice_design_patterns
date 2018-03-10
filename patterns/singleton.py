import logging
from typing import Type

logging.basicConfig(level=logging.INFO)


class Singleton(metaclass=SingletonMeta):
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b


class SingletonMeta(type):
    def __init__(cls: Singleton, name: str, bases: str, attrs: dict):
        cls._singleton = None
        super().__init__(cls, name, bases)

    def __call__(cls, *args: list, **kwargs: dict) -> Singleton:
        if cls._singleton is None:
            cls._singleton = cls.__new__(cls, *args, **kwargs)
        return cls._singleton
