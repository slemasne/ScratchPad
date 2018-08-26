import unittest
from main import  Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        answer = self.calc.sum(2, 4)
        self.assertEquals(answer, 6)

if __name__ == "__main__":
     unittest.main()