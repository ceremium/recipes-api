"""
Tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def test_add_two_numbers_returns_sum(self):
        """Test adding two numbers returns sum"""
        res = calc.add(5, 7)
        self.assertEquals(res, 12)

    def test_subtracing_two_numbers_returns_result(self):
        """Test subtracting two numbers returns sum"""
        res = calc.subtract(12, 5)
        self.assertEquals(res, 7)
