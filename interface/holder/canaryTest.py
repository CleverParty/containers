from django.test import TestCase
from views import index
from sympy import * 
import unittest

def testIndex(val):
    y = Symbol('y')
    func = val
    return(func.diff(y))

class TestStringMethods(unittest.TestCase):
    def test(self):
        y = Symbol('y')
        self.assertEqual(5*y, 5)

if __name__ == '__main__':
    unittest.main()