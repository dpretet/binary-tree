#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import unittest

CURDIR = os.path.abspath(os.path.dirname(__file__))
print CURDIR
sys.path.append(CURDIR+"/../src")
from binary_tree import node, printTree

import random
from datetime import datetime

class BasicTest(unittest.TestCase):
    """ Class description """

    def setUp(self):
        pass

    def tearnDown(self):
        pass

    def test_load(self):
        """ Just test to load the object """
        tree = node()

class PerfMeasure(unittest.TestCase):
    """ Class description """

    def setUp(self):
        pass

    def tearnDown(self):
        pass

    def test_getMin_measure(self):
        """Just test to load the object"""

        tree = node()
        data = []

        for i in range(50000):
            data.append(random.randrange(0, 1001, 1))
        
        for d in data:
            tree.insert(d)

        print ""
        #print data
        print ""
        #printTree(tree, 0)

        dt0 = datetime.now()
        dt0 = dt0.microsecond
        mini = tree.getMinValue()
        dt1 = datetime.now()
        dt1 = dt1.microsecond
        time = dt1 - dt0

        print "tree getMinValue: %d; time: %d" % (mini, time)

        (val, time) = self.getMinValue(data)

        print "basic getMinValue: %d; time: %d" % (val, time)

    def getMinValue(self, listVal):

        minimum = 10000
        dt0 = datetime.now()
        dt0 = dt0.microsecond

        for val in listVal:
            if val < minimum:
                minimum = val

        dt1 = datetime.now()
        dt1 = dt1.microsecond
        time = dt1 - dt0
        return minimum, time


if __name__ == '__main__':

    unittest.main()


