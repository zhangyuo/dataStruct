#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2020-03-24 10:22
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : 5_balanced_binary_tree.py
# @Software : PyCharm
# @Desc     :
"""

"""
平衡二叉树：

是一种严格的自平衡二叉树

又称AVL树，指的是左子树上的所有节点的值都比根节点的值小，而右子树上的所有节点的值都比根节点的值大，且左子树与右子树的高度差最大为1。
因此，平衡二叉树满足所有二叉排序（搜索）树的性质。
至于AVL，则是取自两个发明平衡二叉树的科学家的名字：G. M. Adelson-Velsky和E. M. Landis。

插入的序列越接近有序，生成的二叉搜索树就越像一个链表。
为了避免二叉搜索树变成“链表”，我们引入了平衡二叉树，即让树的结构看起来尽量“均匀”，左右子树的节点数尽量一样多。

二叉树高度平衡被破坏：
添加节点与删除节点
1、LL是left-left，可以理解为：首先它不平衡，其次根节点的左子树比右子树高，并且 根节点的左子树的左子树 比 根节点的左子树的右子树 高。
2、LR是left-right，可以理解为：首先它不平衡，其次根节点的左子树比右子树高，并且 根节点的左子树的右子树 比 根节点的左子树的左子树 高。
3、RR是right-right，可以理解为：首先它不平衡，其次根节点的右子树比左子树高，并且 根节点的右子树的右子树 比 根节点的右子树的左子树 高。
4、RL是right-left，可以理解为：首先它不平衡，其次根节点的右子树比左子树高，并且 根节点的右子树的左子树 比 根节点的右子树的右子树 高。
见README.md "3 平衡二叉树调整"

AVL树的高度是：
O(log n)

AVL树可以使时间复杂度：
O(log n)
"""

from tree.tree_build.tree_node import TreeNode

class AvlTree(object):

    def isBalanced(self, node):
        """
        输入一棵二叉树，判断该二叉树是否是平衡二叉树
        :param node:
        :return:
        """
        if node is None:
            return True
        if abs(self.maxDepth(node.left) - self.maxDepth(node.right)) > 1:
            return False
        return self.isBalanced(node.left) and self.isBalanced(node.right)

    def maxDepth(self, node):
        """
        判断二叉树最大深度
        :param node:
        :return:
        """
        if node is None:
            return 0
        return max(self.maxDepth(node.left), self.maxDepth(node.right)) + 1

    def rebalanced(self, node):
        """
        调整不平衡二叉树为平衡二叉树
        :param node:
        :return:
        """
        # 判断树节点是否为空 & 二叉树是否平衡
        if node and not self.isBalanced(node):
            if self.left_height(node) > self.right_height(node) and self.left_height(node.left) > self.right_height(node.right):
                # LL的情况，只有自己和左孩子的高度可能变化
                node = self._left_left(node, node.left)
            elif self.left_height(node) < self.right_height(node) and self.left_height(node.left) < self.right_height(node.right):
                # RR的情况，只有自己和右孩子的高度可能变化
                node = self._right_right(node, node.right)
            elif self.left_height(node) > self.right_height(node) and self.left_height(node.left) < self.right_height(node.right):
                # LR的情况，只有自己和左孩子和左孩子的右孩子的高度可能变化
                node = self._left_right(node, node.left)
            elif self.left_height(node) < self.right_height(node) and self.left_height(node.left) > self.right_height(node.right):
                # RL的情况，只有自己和右孩子和右孩子的左孩子的高度可能变化
                node = self._right_left(node, node.right)

            # 递归遍历左右子树的平衡情况
            node.left = self.rebalanced(node.left)
            node.right = self.rebalanced(node.right)

        return node

    def left_height(self, node):
        """
        判断左子树的高度
        :param node:
        :return:
        """
        if node.left is not None:
            return self.maxDepth(node.left)

    def right_height(self, node):
        """
        判断右子树的高度
        :param node:
        :return:
        """
        if node.right is not None:
            return self.maxDepth(node.right)

    @staticmethod
    def _left_left(a, b):
        """
        左旋
        例子见LL1和LL2
        :param a: root
        :param b:
        :return:
        """
        a.left = b.right  # 将b的右子树接到a的左子结点上
        b.right = a  # 将a树接到b的右子结点上
        return b

    @staticmethod
    def _right_right(a, b):
        """
        右旋
        例子见RR1
        :param a: root
        :param b:
        :return:
        """
        a.right = b.left
        b.left = a
        return b

    @staticmethod
    def _left_right(a, b):
        """
        a的左子树较高，新结点插入在a的左子树的右子树。先进行左旋转，再进行右旋转
        :param a: root
        :param b:
        :return:
        """
        c = b.right
        a.left, b.right = c.right, c.left
        c.left, c.right = b, a
        return c

    @staticmethod
    def _right_left(a, b):
        """
        a的右子树较高，新结点插入在a的右子树的左子树。先进行右旋转，再进行左旋转
        :param a: root
        :param b:
        :return:
        """
        c = b.left
        a.right, b.left = c.left, c.right
        c.left, c.right = a, b
        return c


if __name__ == "__main__":

    """
    定义一个二叉搜索树
                      18
                13          21
            7      15   19      100
        3      10
    1
    """
    tree = TreeNode(18, TreeNode(13, TreeNode(7, TreeNode(3, TreeNode(1)), TreeNode(10)), TreeNode(15)), TreeNode(21, TreeNode(19), TreeNode(100)))

    avl = AvlTree()
    print("输入一棵二叉树，判断该二叉树是否是平衡二叉树:", avl.isBalanced(tree))
    print("判断二叉树最大深度：", avl.maxDepth(tree))
    print("判断二叉树左子树深度：", avl.left_height(tree))
    print("判断二叉树右子树深度：", avl.right_height(tree))
    new_tree = avl.rebalanced(tree)
    print(avl.isBalanced(new_tree))

