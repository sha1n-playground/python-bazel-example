from enum import Enum

from pypackage.example.nested.module import get


class Status(Enum):  # Enum requires python 3
    A = 1
    B = 2


def what():
    return "example + " + get()
