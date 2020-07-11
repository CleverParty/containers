from django.test import TestCase
from views import index
from sympy import * 
import unittest

class TestStringMethods(unittest.TestCase):

    def testIndex(self):
        y = Symbol('x')
        func = 5*y**3+12
        diffVal = func.diff(y)

if __name__ == '__main__':
    unittest.main()