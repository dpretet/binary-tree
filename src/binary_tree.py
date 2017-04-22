#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    A binary tree implementation
"""

class node(object):
    """ 
    Mother class to create 
    a node in the tree
    """
    
    def __init__(self, value=None):
        """ Class constructor """
        
        # Left node, storing a value smaller/equal
        # of the current node value
        self.left = None
        
        # Right node, storing value greater
        # than current value
        self.right = None
        
        # Node value
        if value is not None:
            self.value = value
        else:
            self.value = None

    def insert(self, value):
        """
        Insert a new value in the node
        """
        if self.value == None:
            self.value = value
            return 0
        else:
            if self.value <= value:
                if self.left == None:
                    self.left = node()
                return self.left.insert(value)
            else:
                if self.right == None:
                    self.right = node()
                return self.right.insert(value)
    
    def lookup(self, value):
        """
        Evaluate a node is equale to value
        """
        if self.value == value:
            return 1
        else:
            return 0

    def _isSmaller(self, value):
        """
        Search for smaller value
        """
        pass

    def _isBigger(self, value):
        """
        Search for bigger value
        """
        pass

    def _isEqual(self, value):
        """
        Check if node value is equal or not
        """

class tree(object):
    """
    A tree object to construct a data structure
    """

    def __init__(self):
        """ Class constructor """
        root = node()

    def rebuild(self):
        """ Rebuild a tree """
        return None

