import sys, os

sys.stderr.write("@@@" + str(sys.argv) + "\n")
elements = os.environ["PYTHONPATH"].split(":")
for element in elements:
    print("@@@" + element)
# sys.stderr.write("###" + str(os.environ["PYTHONPATH"]) + "\n")

import unittest
from pypackage.example.nested.module import get


class ExampleTest(unittest.TestCase):

    def test_get(self):
        self.assertEqual("nested", get())


if __name__ == '__main__':
    unittest.main()
