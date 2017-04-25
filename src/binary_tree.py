#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A binary tree implementation
"""

import sys

class node(object):

    """
    Mother class to create
    a node in the tree
    """

    def __init__(self):
        """ Class constructor """

        # Left node, storing a value smaller/equal
        #  value of the current node value
        self.left = None

        # Right node, storing value greater
        # value than current value
        self.right = None

        # Node value
        self.value = None

    def insert(self, value):
        """
        Insert a new value in the node
        """
        if self.value == None:
            self.value = value
            return None
        else:
            if value <= self.value:
                if self.left == None:
                    self.left = node()
                return self.left.insert(value)
            else:
                if self.right == None:
                    self.right = node()
                return self.right.insert(value)

    def lookup(self, value):
        """
        Evaluate a node is equal to value
        """
        if self.value == None:
            return 0
        elif self.value == value:
            return 1
        else:
            if value <= self.value:
                return self.left.lookup(value)
            else:
                return self.right.lookup(value)

    def getSize(self):
        """
        Return the size of the tree,
        from the current node
        """

        size = 0

        if self.left is not None:
            size = size + self.left.getSize()

        if self.right is not None:
            size = size + self.right.getSize()

        return size

    def getDepth(self):
        """
        Return the depth of the tree,
        from the current node
        """

        depth = 1
        depth_left = 0
        depth_right = 0

        if self.left is not None:
            depth_left = self.left.getDepth()

        if self.right is not None:
            depth_right = self.right.getDepth()

        if depth_left < depth_right:
            depth = depth + depth_right
        else:
            depth = depth + depth_left

        return depth

    def getMinValue(self):
        """
        Return the minimum value of the tree
        """
        val = self.value

        if self.left is not None:
            _val = self.left.getMinValue()
            if _val < val:
                val = _val

        return val

    def getMaxValue(self):
        """
        Return the maximum value of the tree
        """

        val = self.value

        if self.right is not None:
            _val = self.right.getMaxValue()
            if _val > val:
                val = _val

        return val

def printTree(node, sp=0):
    """
    Print the tree
    """
    ret = {"level" : sp, "val" : ".", "left" : ".", "right" : "."} 

    if node is not None:
        
        ret["val"] = node.value
        
        if node.left is not None:
            #print printTree(node.left, sp+1)
            ret["left"] =  printTree(node.left, sp+1)
        
        #print str(node.value)
        
        if node.right is not None:
            #print printTree(node.right, sp+1)
            ret["right"] = printTree(node.right, sp+1)

    return ret

