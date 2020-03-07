# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:06:58 2020

@author: k8958
"""

import unittest

def addition(a,b):
    return a+b
class UnitTest(unittest.TestCase):
    def test(self):
        self.assertEqual(addition(2,3),4) 





if __name__ == '__main__':
    unittest.main()