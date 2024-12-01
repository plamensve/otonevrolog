from django.test import TestCase


def sum_two_numbers(num1, num2):
    return num1 + num2


class TestSumTwoNumbers(TestCase):
    def test_sum_two_numbers(self):
        result = sum_two_numbers(4, 5)
        expected = 9

        self.assertEqual(result, expected)
