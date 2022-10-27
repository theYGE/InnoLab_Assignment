import unittest
from src.innolab_package_Oleksandr_Makarevych.main import kaya_equation

class TestKayaEquation(unittest.TestCase):
    def test_value(self):
        actual = kaya_equation(1,2,3,4)
        expected = 1 * 2 * 3 * 4
        self.assertEqual(actual, expected)

    def test_value_c(self):
        actual = kaya_equation(1, 2, 3, 10, output_type="C")
        expected = 1 * 2 * 3 * 10 / 3.67
        self.assertEqual(actual, expected)

    def test_value_c_1(self):
        actual = kaya_equation(1, 2, 30, 10, output_type="C")
        expected = 1 * 2 * 30 * 10 / 3.67
        self.assertEqual(actual, expected)

    def test_raise_error(self):
        with self.assertRaises(ValueError) as exception_context:
            kaya_equation(-1, 2, 3, 4)
        self.assertEqual(
            str(exception_context.exception),
            "pop cannot be negative"
        )
