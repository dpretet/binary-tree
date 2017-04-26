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

def getTree(tree, depth=0):
    """
    Get the tree in a nested dictionnary
    """
    node = {"depth" : depth, "value" : None, "left" : None, "right" : None}
    max_depth = depth
    max_depth_left = depth
    max_depth_right = depth

    if tree is not None:
        
        node["value"] = tree.value
        
        if tree.left is not None:
            max_depth_left, node["left"] =  getTree(tree.left, depth+1)
        
        if tree.right is not None:
            max_depth_right, node["right"] = getTree(tree.right, depth+1)
    if max_depth < max_depth_left:
        max_depth = max_depth_left
    if max_depth < max_depth_right:
        max_depth = max_depth_right
    return max_depth, node

def printTree(tree):
    """
    Print the tree
    """
    max_depth, nested_tree = getTree(tree, 0)
    string_tree = []
    
    for i in range(max_depth+1):
        string_tree.append("")
    
    outtree = _printTree(nested_tree, 0, max_depth, string_tree)
    
    for line in outtree:
        print line
    #print max_depth
    #print outtree

def _printTree(tree, depth, max_depth, string_tree):
    """
    Internal print tree
    """

    if tree is not None:
        if "value" in tree and tree["value"] is not None:
            string_tree[depth] += (max_depth-depth)*"  " + str(tree["value"]) + " "
            string_tree = _printTree(tree["left"], tree["depth"]+1, max_depth, string_tree)
            string_tree = _printTree(tree["right"], tree["depth"]+1, max_depth, string_tree)
    return string_tree
