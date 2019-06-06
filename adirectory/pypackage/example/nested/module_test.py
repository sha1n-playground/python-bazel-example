import unittest

from pypackage.example.nested.module import get


class ExampleTest(unittest.TestCase):

    def test_get(self):
        self.assertEqual("nested", get())


if __name__ == '__main__':
    unittest.main()
