#!/usr/bin/python
# author luke

RED = 0
BLACK = 1


# 左旋，tree是树对象，node是要调整的节点
def left_rotate(tree, node):
    # 防止用户搞错了
    if not node.right:
        return False
    node_right = node.right
    node_right.p = node.p
    # node是根，就要修改根
    if not node.p:
        tree.root = node_right
    # 看node是G的左孩子，那么node_right就要作为G的左孩子
    elif node == node.p.left:
        node.p.left = node_right
    # 看node是G的右孩子，那么node_right就要作为G的右孩子
    else:
        node.p.right = node_right
    # 判断node_right是否有左孩子，如果有，那么变为node的右孩子
    if node_right.left:
        node_right.left.p = node
    # 变为node的右孩子，没孩子给的是None
    node.right = node_right.left
    node.p = node_right
    node_right.left = node


# 右旋
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
        if direction == 0:  # tree是根节点
            print("%2d(B) is root" % node.value)
        else:  # tree是分支节点
            print("%2d(%s) is %2d's %6s child" % (
                node.value, ("B" if node.color == 1 else "R"), key, ("right" if direction == 1 else "left")))

        rbtree_print(node.left, node.value, -1)
        rbtree_print(node.right, node.value, 1)


class RedBlackTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.p = None  # 父亲的藏宝图
        self.color = RED  # 放入节点默认是红色


class RBTree:

    def __init__(self):
        self.root = None

    # 通过二叉查找，找到位置
    def insert(self, node_value):
        new_node = RedBlackTreeNode(node_value)
        temp_cur=self.root
        #遍历二叉树，找到要放的节点的位置
        while temp_cur:
            insert_pos_parent=temp_cur
            if temp_cur.value <new_node.value:
                temp_cur=temp_cur.right
            else:
                temp_cur=temp_cur.left

        #要判断根为不为空
        if not self.root:
            self.root=new_node
            new_node.color=BLACK
            return
        else:
            if insert_pos_parent.value>=new_node.value:
                insert_pos_parent.left=new_node
            else:
                insert_pos_parent.right=new_node
            new_node.p=insert_pos_parent

        self.insert_fixup(new_node)

    def insert_fixup(self,new_node):
        while new_node.p and new_node.p.color==RED:
            parent=new_node.p
            grandparent=parent.p
            #这是父亲在爷爷的左边的情形3,4,5
            if grandparent.left == parent:
                #情形三
                uncle=grandparent.right
                if uncle and uncle.color==RED:
                    parent.color=BLACK
                    uncle.color=BLACK
                    grandparent.color=RED
                    new_node=grandparent
                    continue
                #情形四
                if parent.right == new_node:
                    left_rotate(self,parent)
                    parent,new_node=new_node,parent
                # 情形五
                right_rotate(self,grandparent)
                grandparent.color=RED
                parent.color=BLACK
            else:
                #情形三
                uncle=grandparent.left
                if uncle and uncle.color==RED:
                    parent.color=BLACK
                    uncle.color=BLACK
                    grandparent.color=RED
                    new_node=grandparent
                    continue
                #情形四
                if parent.left == new_node:
                    right_rotate(self,parent)
                    parent,new_node=new_node,parent
                # 情形五
                left_rotate(self,grandparent)
                grandparent.color=RED
                parent.color=BLACK

        self.root.color=BLACK

#今天写的
if __name__ == '__main__':
    data = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    tree = RBTree()
    for i in data:
        tree.insert(i)

    rbtree_print(tree.root, tree.root.value, 0)