from django.test import TestCase
from views import index
from sympy import * 
import unittest

class TestStringMethods(unittest.TestCase):

    def testIndex(self):
        y = Symbol('x')
        func = 5*y
        diffVal = func.diff(y)
    
    def test(self):
        self.assertEqual(self.testIndex(), 5)

if __name__ == '__main__':
    unittest.main()