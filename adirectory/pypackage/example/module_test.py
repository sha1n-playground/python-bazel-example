import platform
import unittest

from pypackage.example.module import what


class ExampleTest(unittest.TestCase):

    def test_me(self):
        self.assertEqual("example + nested", what())

    def test_platform_version(self):
        self.assertEqual("3", platform.python_version_tuple()[0])


if __name__ == '__main__':
    unittest.main()
