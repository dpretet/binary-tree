#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

CURDIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(CURDIR + "/../src")
from binary_tree import node

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
        del tree


class PerfMeasure(unittest.TestCase):
    """ Class description """

    def setUp(self):
        pass

    def tearnDown(self):
        pass

    def test_getMinValue_measure(self):
        """Just test to load the object"""

        tree = node()
        data = []

        for i in range(10000):
            data.append(random.randrange(0, 101, 1))

        for d in data:
            tree.insert(d)

        # print data
        # printTree(tree)

        dt0 = datetime.now()
        dt0 = dt0.microsecond
        mini = tree.getMinValue()
        dt1 = datetime.now()
        dt1 = dt1.microsecond
        time = dt1 - dt0

        print "BTS getMinValue time: %d; time: %d ms" % (mini, time)

        (mini, time) = self.getMinValue(data)

        print "Basic list getMinValuetime: %d; time: %d ms" % (mini, time)

    def getMinValue(self, listVal):

        mini = 10000
        dt0 = datetime.now()
        dt0 = dt0.microsecond

        for val in listVal:
            if val < mini:
                mini = val

        dt1 = datetime.now()
        dt1 = dt1.microsecond
        time = dt1 - dt0

        return mini, time


if __name__ == '__main__':

    unittest.main()
