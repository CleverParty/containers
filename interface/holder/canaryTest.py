from django.test import TestCase
from views import index
from sympy import * 
import unittest

def testIndex(val):
    x = Symbol('x')
    f = val
    d = f.diff(x)
    return(d)

class TestStringMethods(unittest.TestCase):
    def test(self):
        x = Symbol('x')
        testCheck = 10*x
        testVal = 5*x**2+12
        print(testIndex(testVal))
        self.assertEqual(testIndex(testVal), testCheck)

if __name__ == '__main__':
    unittest.main()