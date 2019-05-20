#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import random
from binary_tree import Node
from binary_tree import display
import os
import sys
import unittest

CURDIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(CURDIR + "/../src")


class BasicTest(unittest.TestCase):
    """ Class description """

    def setUp(self):
        pass

    def tearnDown(self):
        pass

    def test_load(self):
        """ Just test to load the object """
        tree = Node()
        del tree


class PerfMeasure(unittest.TestCase):
    """ Class description """

    def setUp(self):
        pass

    def tearnDown(self):
        pass

    def test_getMinValue_measure(self):
        """Just test to load the object"""

        tree = Node()
        data = []

        for i in range(10000):
            data.append(random.randrange(0, 101, 1))

        for d in data:
            tree.insert(d)

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


class Display(unittest.TestCase):
    """ Class description """

    def setUp(self):
        pass

    def tearnDown(self):
        pass

    def test_getMinValue_measure(self):
        """Just test to load the object"""

        tree = Node()
        data = []

        for i in range(30):
            d = random.randrange(0, 101, 1)
            if d not in data:
                data.append(d)

        for d in data:
            if not tree.lookup(d):
                print("Insert %d in the tree" % d)
                tree.insert(d)

        display(tree)


if __name__ == '__main__':

    unittest.main()
