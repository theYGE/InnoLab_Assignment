import unittest
from main import kaya_equation

class TestKayaEquation(unittest.TestCase):
    def value_test(self):
        actual = kaya_equation(1,2,3,4)
        expected = 1 * 2 * 3 * 4
        self.assertEqual(actual, expected)
