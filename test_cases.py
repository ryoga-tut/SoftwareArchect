#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (200, calc(2,100))

        def test_sample2 (self):
                self.assertEqual (-1, calc(1000,1))

        def test_sample3 (self):
                self.assertEqual (-1, calc('abc','d'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.5,5))
        
        def test_sample5 (self):
                self.assertEqual (-1, calc('a',5))
        
        def test_sample6 (self):
                self.assertEqual (-1, calc(0.5, 0.2))
        
        def test_sample4 (self):
                self.assertEqual (-1, calc(1000, 0.5))

