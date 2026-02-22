from django.test import  SimpleTestCase
from app import calc

class CalcTestCase(SimpleTestCase):
    def test_add(self):
        res = calc.add(2, 3)
        self.assertEqual(res, 5)
        
    def test_subtract(self):
        res = calc.subtract(5, 2)
        self.assertEqual(res, 3)