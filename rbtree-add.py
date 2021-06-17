#!/usr/bin/python
# author yuanquan
RED = 0
BLACK = 1



def left_rotate(tree, node):

    if not node.right:
        return False
    node_right = node.right
    node_right.p = node.p

    if not node.p:
        tree.root = node_right

    elif node == node.p.left:
        node.p.left = node_right

    else:
        node.p.right = node_right

    if node_right.left:
        node_right.left.p = node

    node.right = node_right.left
    node.p = node_right
    node_right.left = node



def right_rotate(tree, node):
    if not node.left:
        return False
    node_left = node.left
    node_left.p = node.p
    if not node.p:
        tree.root = node_left
    elif node == node.p.left:
        node.p.left = node_left
    elif node == node.p.right:
        node.p.right = node_left
    if node_left.right:
        node_left.right.p = node
    node.left = node_left.right
    node.p = node_left
    node_left.right = node



def rbtree_print(node, key, direction):
    if node:
        if direction == 0:
            print("%2d(B) is root" % node.value)
        else:
            print("%2d(%s) is %2d's %6s child" % (
                node.value, ("B" if node.color == 1 else "R"), key, ("right" if direction == 1 else "left")))

        rbtree_print(node.left, node.value, -1)
        rbtree_print(node.right, node.value, 1)


class RedBlackTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.p = None
        self.color = RED


class RBTree:
    def __init__(self):
        self.root: RedBlackTreeNode = None

    def fixup(self, node):
        node_parent: RedBlackTreeNode = node.p
        while node_parent and node_parent.color == RED:
            grand_parent: RedBlackTreeNode = node_parent.p
            if grand_parent.left is node_parent:
                if grand_parent.right and grand_parent.right.color is RED:
                    grand_parent.right.color = BLACK
                    grand_parent.color = RED
                    node_parent.color = BLACK
                    node = grand_parent
                    node_parent = node.p
                    continue
                if node_parent.right is node:
                    left_rotate(self, node_parent)
                    node_parent, node = node, node_parent
                right_rotate(self, grand_parent)
                node_parent.color = BLACK
                grand_parent.color = RED
            else:
                if grand_parent.left and grand_parent.left.color is RED:
                    grand_parent.left.color = BLACK
                    grand_parent.color = RED
                    node_parent.color = BLACK
                    node = grand_parent
                    node_parent = node.p
                    continue
                if node_parent.left is node:
                    right_rotate(self, node_parent)
                    node_parent, node = node, node_parent
                left_rotate(self, grand_parent)
                node_parent.color = BLACK
                grand_parent.color = RED
        self.root.color=BLACK

    def insert(self, value):
        new_node = RedBlackTreeNode(value)
        node_parent = None
        current_node = self.root
        while current_node:
            node_parent = current_node
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        if self.root == None:
            self.root = new_node
            self.root.color=BLACK
        else:
            new_node.p = node_parent
            if new_node.value > node_parent.value:
                node_parent.right = new_node
            else:
                node_parent.left = new_node
            self.fixup(new_node)


if __name__ == '__main__':
    data = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    tree = RBTree()
    for i in data:
        tree.insert(i)
        rbtree_print(tree.root, tree.root.value, 0)
