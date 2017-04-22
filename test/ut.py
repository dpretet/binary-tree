#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import unittest

CURDIR = os.path.abspath(os.path.dirname(__file__))
print CURDIR
sys.path.append(CURDIR+"/../src")
from binary_tree import node

class BasicTest(unittest.TestCase):
    """ Class description """
    
    def setUp(self):
        pass

    def tearnDown(self):
        pass
    
    def test_load(self):
        """ Just test to load the object """
        n = node()


if __name__ == '__main__':

    unittest.main()
    

