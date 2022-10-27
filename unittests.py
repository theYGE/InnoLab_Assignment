import unittest
from main import kaya_equation

class TestKayaEquation(unittest.TestCase):
    def test_value(self):
        actual = kaya_equation(1,2,3,4)
        expected = 1 * 2 * 3 * 4
        self.assertEqual(actual, expected)

    def test_raise_error(self):
        with self.assertRaises(ValueError) as exception_context:
            kaya_equation(-1, 2, 3, 4)
        self.assertEqual(
            str(exception_context.exception),
            "pop cannot be negative"
        )
