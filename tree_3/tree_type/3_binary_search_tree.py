#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2020-02-11 14:41
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : binarySearchTree.py
# @Software : PyCharm
# @Desc     :
"""

"""
二叉搜索树(Binary Search Tree, BST)，也称为二叉查找树、二叉排序树

它在二叉树上施加了排序的顺序，一棵非空二叉搜索树有以下性质：
非空左子树所有节点数据项小于其根节点的数据项；非空右子树所有节点数据项大于其根节点的数据项；左右子树都是二叉搜索树。

查找是数据结构中常用的操作，所谓查找就是根据给定的项item，从集合中找出与给定项item相同的记录。查找的算法有多种，二分查找是效率较高的查找方式。
查找分为静态查找和动态查找。
所谓静态查找是指集合中的记录是固定的，没有删除和插入的操作，只能进行查找。很显然，二分查找就是静态查找的一种方式；
所谓动态查找是指集合中的记录是动态变化的，不仅有较高的查找效率，对插入和删除操作也有较高的效率。
那么针对于动态查找数据应该如何组织呢，二叉搜索树就是动态查找的数据存储方式。

二叉搜索树：
平均深度为O(logN)

缺点：
二叉搜索树的结构与值的插入顺序有关。见README.md "二叉树插入顺序`"
"""

from tree_3.tree_build.tree_node import TreeNode


class BinSerTree(object):

    def find(self, node, item):
        """
        二叉搜索树：查找操作-查找树节点
        :param node:
        :param item:
        :return:
        """
        if node is None:
            return False
        elif item < node.item:
            return self.find(node.left, item)
        elif item > node.item:
            return self.find(node.right, item)
        else:
            return True

    def findMin(self, node):
        """
        二叉搜索树：查找最小值
        :param node:
        :return:
        """
        if node is None:
            return None
        elif node.left is None:
            return node.item
        else:
            return self.findMin(node.left)

    def findMax(self, node):
        """
        二叉搜索树：查找最小值
        :param node:
        :return:
        """
        if node is None:
            return None
        elif node.right == None:
            return node.item
        else:
            return self.findMax(node.right)

    def inorder(self, node):
        """
        二叉搜索树：中序遍历-递归实现
        :param node:
        :return:
        """
        if node is None:
            return []
        result = [node.item]
        left_item = self.inorder(node.left)
        right_item = self.inorder(node.right)
        return left_item + result + right_item

    def inorder_stack(self, node):
        """
        二叉搜索树：中序遍历-堆栈实现/stack_6/优先队列（一种数据项按序排列的数据结构，只能在一端(称为栈顶(top))对数据项进行插入和删除，
        严格按照“先进后出”的原则存取）
        :param node:
        :return:
        """
        if node is None:
            return []
        result = []
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.item)
            node = node.right
        return result

    """
    二叉搜索树的插入元素操作
    关键是找出元素要插入的位置，可以采取类似于查找的方法，判断当前节点数据项和要插入元素的大小以确定要插入元素的位置，
    对于BST通过中序遍历会得到从小到大排列的节点数据元素。
    """

    def insert(self, node, item):
        """
        也能构建二叉搜索树
        向二叉搜索树中插入元素
        :param node:
        :return:
        """
        if node is None:
            node = TreeNode(item)
        elif item < node.item:
            node.left = self.insert(node.left, item)
        else:
            node.right = self.insert(node.right, item)
        return node

    """
    二叉搜索树的删除元素操作
    三种情况：
    1、要删除节点为叶子节点，直接删除节点，并修改父节点对应的指针为空
    2、要删除节点只有一个孩子，直接删除节点，将节点的指针指向孩子节点
    3、要删除节点有两个孩子，用另一个节点（左子树最大元素或右子树最小元素）去代替被删除节点
    """

    def delete(self, node, item):
        """
        二叉搜索树中删除元素
        :param node:
        :param item:
        :return:
        """
        if node is None:
            return None
        elif node.item > item:
            node.left = self.delete(node.left, item)  # 递归查找待删除元素
        elif node.item < item:
            node.right = self.delete(node.right, item)  # 递归查找待删除元素
        else:
            if node.right and node.left:  # 第三种情况
                # 用右子树最小元素替代被删除节点
                node.item = self.findMin(node.right)
                # 递归删除右子树最小节点
                node.right = self.delete(node.right, node.item)
            else:
                if node.right == None:  # 第二种情况
                    node = node.left
                elif node.left == None:  # 第二种情况
                    node = node.right
        return node

    def tree_depth(self, node):
        """
        计算二叉树深度
        :param node:
        :return:
        """
        if node is None:
            return 0
        left_count = self.tree_depth(node.left)
        right_count = self.tree_depth(node.right)

        if left_count >= right_count:
            return left_count + 1
        else:
            return right_count + 1


if __name__ == '__main__':
    """
    定义一个二叉搜索树
                  18
            13          21
        7      15   19      100
    3      10
    """
    tree = TreeNode(18, TreeNode(13, TreeNode(7, TreeNode(3), TreeNode(10)), TreeNode(15)),
                    TreeNode(21, TreeNode(19), TreeNode(100)))

    bin_ser_tree = BinSerTree()
    print("二叉搜索树：查找数值：")
    print(bin_ser_tree.find(tree, 21))
    print(bin_ser_tree.find(tree, 101), '\n')

    print("二叉搜索树：查找最大值：")
    print(bin_ser_tree.findMin(tree))

    print("二叉搜索树：查找最小值：")
    print(bin_ser_tree.findMax(tree), '\n')

    print("中序遍历-递归实现：")
    print(bin_ser_tree.inorder(tree))

    print("中序遍历-堆栈实现：")
    print(bin_ser_tree.inorder_stack(tree), '\n')

    print("向二叉搜索树中插入元素：")
    print(bin_ser_tree.inorder(bin_ser_tree.insert(tree, 80)))
    print("构建二叉搜索树：")
    tree = None
    tree = bin_ser_tree.insert(tree, 80)
    tree = bin_ser_tree.insert(tree, 3)
    tree = bin_ser_tree.insert(tree, 12)
    tree = bin_ser_tree.insert(tree, 8)
    tree = bin_ser_tree.insert(tree, 81)
    tree = bin_ser_tree.insert(tree, 56)
    print(bin_ser_tree.inorder(tree), '\n')

    print("二叉搜索树中删除元素：")
    print(bin_ser_tree.inorder(bin_ser_tree.delete(tree, 80)), '\n')

    print("二叉树深度")
    print(bin_ser_tree.tree_depth(tree))
