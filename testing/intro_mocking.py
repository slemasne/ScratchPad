import unittest
from main import Calculator
from unittest.mock import patch

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_subtract(self):
        answer = self.calc.subtract(10, 4)
        self.assertEquals(answer, 6)

    @patch.object(Calculator, '_Calculator__sum', return_value = 9)
    def test_sum(self, sum):
        self.assertEquals(sum(2,3), 9)

if __name__ == "__main__":
     unittest.main()