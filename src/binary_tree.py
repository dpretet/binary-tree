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
    
    def __init__(self):
        """ Class constructor """
        
        # Left node, storing a value smaller/equal
        # current node value
        self.left = None
        # Right node, storing value greater
        # than current value
        self.right = None
        # Node value
        self.value = None

    def insert(self, value):
        """
        Insert a new value in the node
        """
        pass

    def remove(self):
        """
        Remove a value in the node
        """
        pass
    
    def equal(self, value):
        """
        Search for equal value
        """
        pass

    def smaller(self, value):
        """
        Search for smaller value
        """
        pass

    def bigger(self, value):
        """
        Search for bigger value
        """
        pass


