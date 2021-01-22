#!/usr/bin/env python
# coding:utf-8
"""
# @Time     : 2020-02-11 13:56
# @Author   : Zhangyu
# @Email    : zhangycqupt@163.com
# @File     : binarytree.py
# @Software : PyCharm
# @Desc     :
"""

"""
二叉树：

特点：
1 每个结点最多2个子树，二叉树不存在度数大于2的节点
2 它是有序树，左子树，右子树是顺序的，不能交换次序
3 即使某一个结点只有一颗子树，也要确定其是左子树还是右子树

二叉树的五种形态：
1 空二叉树
2 只有一个根结点
3 根结点只有左子树
4 根结点只有右子树
5 根结点有左子树和右子树

满二叉树：
一颗二叉树的所有分支结点都存在左子树和右子树，且所有叶子节点都只存在在最下面一层。
同样深度的二叉树，满二叉树节点最多
k为深度(1<=k<=n)，则节点总数为 2**(k)-1

完全二叉树：
若二叉树的深度为k，二叉树的层数从1到k-1层的结点都打到了最大个数，在第k层的所有结点都集中在最左边，这就是完全二叉树
完全二叉树由满二叉树引出
满二叉树一定是完全二叉树，但完全二叉树不一定是满二叉树
k为深度(1<=k<=n)，则结点总数最大值为2**k-1,当达到最大值的时候就是满二叉树

二叉树性质：
1 在二叉树中的第i层上最多有2**i-1 个节点(i>=1)
2 深度为k的二叉树，至多有2**k -1个节点（k>=1）
3 对于任何一颗二叉树T，如果其终点节点数为n0,度数为2的节点为n2，则有n0=n2+1，及叶子结点数-1=度数为2的节点数。
    证明：
    总结点数为n=n0+n1+n2，其中n0为度数为0的节点，及叶子节点的数量，n1为度数为1 的节点的数量，n2为节点为2度数的数量。
    一棵树的分支数为n-1，因为除了根节点外，其余结点都有一个分支，及n0+n1+n2-1
    分支数还等于n0*0+n1*1+n2*2及 n1+2n2=n-1
    可知 2*n2+n1=n0+n1+n2-1 及就是 n2=n0-1
4 高度为k的二叉树，至少有k个节点
5 具有n个节点的完全二叉树的深度为int(log2n)+1 或者 math.ceil(log2(n+1))
6 有一个n个节点的完全二叉树， 结点按照层序编号:
    (1)如果i=1，则节点i是二叉树的根，无双亲，如果i>1，则其双亲为int(i/2)，向下取整。就是叶子节点的编号整除2得到的就是父节点的编号，
       如果父节点是i，则左孩子是2i，若有右孩子，则右孩子是2i+1,。
    (2)如果2i>n，则结点i无左孩子，及结点为叶子结点，否则其左孩子节点存在编号为2i。
    (3)如果2i+1>n，则节点i无右孩子，此处未说明是否不存在左孩子，否则右孩子的节点存在编号为2i+1

二叉树的遍历：
1 广度优先遍历：一次将一层全部拿完，层序遍历
2 深度优先遍历：设树的根结点为D，左子树为L，右子树为R
  （1）前序遍历，也叫先序遍历，也叫先跟遍历，DLR
  （2）中序遍历，也叫中跟遍历， LDR
  （3）后序遍历，也叫后跟遍历，LRD 

二叉树的构建方法：
1、列表表示
2、节点表示

二叉树的平均深度：
大O根号N
"""

from tree.tree_build.tree_node import TreeNode

"""
创建一个 BinaryTree 的类，定义根节点
"""
class BinaryTree(object):

    def __init__(self):
        self.root = TreeNode('root')  # 根节点定义为 root 永不删除，作为哨兵使用。

    def insert(self, item):
        """
        插入节点
        构建二叉树
        :param item:
        :return:
        """
        node = TreeNode(item)
        if self.root is None:  # 如果二叉树为空，那么生成的二叉树最终为新插入树的点
            self.root = node
        else:
            q = [self.root]  # 将q列表，添加二叉树的根节点
            while True:
                pop_node = q.pop(0)  # 弹出最先进入列表的元素
                if pop_node.left is None:  # 左子树为空则将点添加到左子树
                    pop_node.left = node
                    return
                elif pop_node.right is None:  # 右子树为空则将点添加到右子树
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)
    """
    2_list.pop() 弹出最后一个元素，先进后出-栈-6_stack
    2_list.pop(0) 弹出第一个元素，先进先出-队列-4_queue
    """

    def delete(self, item):
        """
        删除节点
        :param item:
        :return:
        """
        if self.root is None:  # 如果根为空，就什么也不做
            return False

        parent = self.get_parent(item)
        if parent:
            del_node = parent.left if parent.left.item == item else parent.right  # 待删除节点
            if del_node.left is None:
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:
                if parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True
            else:  # 左右子树都不为空
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right

                else:
                    while tmp_next.left:  # 让tmp指向右子树的最后一个叶子
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False

    def get_parent(self, item):
        if self.root.item == item:
            return None  # 根节点没有父节点
        tmp = [self.root]  # 将tmp列表，添加二叉树的根节点
        while tmp:
            pop_node = tmp.pop(0)
            if pop_node.left and pop_node.left.item == item:  # 某点的左子树为寻找的点
                return pop_node  # 返回某点，即为寻找点的父节点
            if pop_node.right and pop_node.right.item == item:  # 某点的右子树为寻找的点
                return pop_node  # 返回某点，即为寻找点的父节点
            if pop_node.left is not None:  # 添加tmp 元素
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return None

    def inorder(self, node):
        """
        中序遍历

        先处理左子树，然后处理当前节点，再处理右子树；
        对于一颗二叉查找树，所有的信息都是有序排列的，中序遍历可以是信息有序输出，且运行时间为 O（n）；
        递归实现中序遍历。
        :param node:
        :return:
        """
        if node is None:
            return []
        result = [node.item]
        left_item = self.inorder(node.left)
        right_item = self.inorder(node.right)
        return left_item + result + right_item

    def postorder(self, node):
        """
        后序遍历

        先处理左右子树，然后再处理当前节点，运行时间为 O（n）
        递归实现后序遍历
        :param node:
        :return:
        """
        if node is None:
            return []
        result = [node.item]
        left_item = self.postorder(node.left)
        right_item = self.postorder(node.right)
        return left_item + right_item + result

    def preorder(self, node):
        """
        先序遍历

        先处理当前节点，再处理左右子树；
        递归实现先序遍历。
        :param node:
        :return:
        """
        if node is None:
            return []
        result = [node.item]
        left_item = self.preorder(node.left)
        right_item = self.preorder(node.right)
        return result + left_item + right_item

    def maxDepth(self, node):
        """
        求二叉树的深度
        :param node:
        :return:
        """
        if node is None:
            return 0
        return max(self.maxDepth(node.left), self.maxDepth(node.right)) + 1


if __name__ == "__main__":
    print("定义树根节点：")
    tree = BinaryTree()
    print(tree, '\n')

    print("插入(数据无序）：")
    tree.insert(2)
    tree.insert(7)
    tree.insert(18)
    tree.insert(4)
    tree.insert(22)
    print(tree, '\n')

    # 中序遍历
    print("中序遍历：")
    print(tree.inorder(tree.root), '\n')

    print("求二叉树的深度：")
    print(tree.maxDepth(tree.root))
