#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A binary tree implementation
"""

from graphviz import Digraph


class Node(object):

    """
    Mother class to create
    a node in the tree
    """

    def __init__(self):
        """ Class constructor """

        # Left node, storing a value smaller/equal
        # value of the current node value
        self.left = None

        # Right node, storing value greater
        # value than current value
        self.right = None

        # Node value
        self.value = None

    def insert(self, value):
        """ Insert a new value in the node """

        if self.value is None:
            self.value = value
            return

        if value <= self.value:
            if self.left is None:
                self.left = Node()

            return self.left.insert(value)

        else:
            if self.right is None:
                self.right = Node()

            return self.right.insert(value)

    def lookup(self, value):
        """ Evaluate a node is equal to value """

        if self.value is None:
            return 0

        if self.value == value:
            return 1

        if self.left is None:
            return 0

        if self.right is None:
            return 0

        if value <= self.value:
            return self.left.lookup(value)

        return self.right.lookup(value)

    def getSize(self):
        """ Return the size of the tree, from the current node """

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
        """ Return the minimum value of the tree """

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
    """ Get the tree in a nested dictionnary """

    node = {"depth": depth, "value": None, "left": None, "right": None}

    max_depth = depth
    max_depth_left = depth
    max_depth_right = depth

    if tree is not None:

        node["value"] = tree.value

        if tree.left is not None:
            max_depth_left, node["left"] = getTree(tree.left, depth + 1)

        if tree.right is not None:
            max_depth_right, node["right"] = getTree(tree.right, depth + 1)

    if max_depth < max_depth_left:
        max_depth = max_depth_left

    if max_depth < max_depth_right:
        max_depth = max_depth_right

    return max_depth, node


def display(tree):
    """ Display the created graph,
    rendered with Graphviz """

    dot = Digraph('g', filename='btree.gv', node_attr={'shape': 'record', 'height': '.1'})
    _addNodeNEdge(dot, tree)
    dot.render('tree', view=True)


def _addNodeNEdge(dot, node):
    """ Recursive function to add a node,
    its value and children """

    print("Process %d" % node.value)
    dot.node(str(node.value))

    if node.left:
        _addNodeNEdge(dot, node.left)
        dot.edge(str(node.value), str(node.left.value), constraint='true')
        print("Add edge from %d to %d" % (node.value, node.left.value))

    if node.right:
        _addNodeNEdge(dot, node.right)
        dot.edge(str(node.value), str(node.right.value), constraint='true')
        print("Add edge from %d to %d" % (node.value, node.right.value))
