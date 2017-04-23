#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import unittest

CURDIR = os.path.abspath(os.path.dirname(__file__))
print CURDIR
sys.path.append(CURDIR+"/../src")
from binary_tree import node

import random

class BasicTest(unittest.TestCase):
    """ Class description """
    
    def setUp(self):
        pass

    def tearnDown(self):
        pass
    
    def test_load(self):
        """ Just test to load the object """
        tree = node()

class ParseTree(unittest.TestCase):
    """ Class description """
    
    def setUp(self):
        pass

    def tearnDown(self):
        pass
    
    def test_create(self):
        """ Just test to load the object """
        data = []
        tree = node()
        
        for i in range(10):
            data.append(random.randrange(0, 101, 1))

        print data
        
        for i in range(len(data)):
            tree.insert(i)

if __name__ == '__main__':

    unittest.main()
    

