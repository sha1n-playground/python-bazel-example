import sys, os

sys.stderr.write("@@@" + str(sys.argv) + "\n")
sys.stderr.write("###" + str(os.environ["PYTHONPATH"]) + "\n")

import unittest
from project.example.nested.nested import nested


class ExampleTest(unittest.TestCase):

    def test_get(self):
        self.assertEqual("nested", nested())


if __name__ == '__main__':
    unittest.main()
