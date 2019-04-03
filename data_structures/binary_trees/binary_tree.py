# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:08:53 2019

@author: Aryan Singh

some points on binary trees - http://cslibrary.stanford.edu/110/BinaryTrees.pdf
    1. Node is the root of the tree
"""

def lookup(node, target):
    if node == None:
        return False
    else:
        if target < node.data:
            return lookup(node.left, target)
        else:
            return lookup(node.right, target)

def newNode(data):
    # have to return a new node here
    return None

def insert(node, data):
    if node is None:
        return newNode(data)
    else:
        if data<node.data:
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)
        return node
    
def size(node):
    if node is None:
        return 0
    else:
        return 1 + size(node.left) + size(node.right)

def maxDepth(node):
    if node is None:
        return 0
    else:
        leftD = maxDepth(node.left)
        rightD = maxDepth(node.right)
        
        return max(leftD, rightD)+1

''' This is a balanced tree, so we just need to traverse left   '''
def minValue(node):
    while node.left is not None:
        node = node.left
    return node.data

'''
 Given a binary tree, print its
 nodes according to the "bottom-up"
 postorder traversal.
'''
def postOrder(node):
    if node is None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.data)
    