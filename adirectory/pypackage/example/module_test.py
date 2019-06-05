import unittest
from pypackage.example.module import what


class ExampleTest(unittest.TestCase):

    def test_me(self):
        self.assertEqual("example + nested", what())


if __name__ == '__main__':
    unittest.main()
