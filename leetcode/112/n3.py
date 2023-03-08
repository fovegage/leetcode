class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.onePath = []
        self.PathArray = []
        self.index = 0
        self.node_data = [10, 5, 4, None, 3, None, None, 7, None, None, 12, None, None]

    def build_node(self):
        current_data = self.node_data[self.index]
        self.index += 1
        # if current_data != None:
        #     node = TreeNode(current_data)
        #     left = self.build_node()
        #     node.left = left
        #     right = self.build_node()
        #     node.right = right
        #     return node

        if current_data != None:
            node = TreeNode(current_data)
            node.left = self.build_node()
            node.right = self.build_node()
            return node

    def FindPath(self, root, expectNumber):
        if root is None:
            return self.PathArray
        self.onePath.append(root.val)
        # 期望值 - 根节点  不断的减去节点的值  不为0 说明还有值  如果刚好为0那么说明找到路径
        expectNumber -= root.val
        if expectNumber == 0 and not root.left and not root.right:
            self.PathArray.append(self.onePath[:])
        elif expectNumber > 0:
            self.FindPath(root.left, expectNumber)
            self.FindPath(root.right, expectNumber)
        # 当期望值小于节点值时，dir仍旧会执行一次append操作，就是因为后面会把这个值pop出去
        # https://www.cnblogs.com/bambipai/p/9901965.html
        self.onePath.pop()
        return self.PathArray

    def loop(self, tree: TreeNode, num):
        if tree is None:
            return self.PathArray
        node_val = tree.val
        self.onePath.append(node_val)
        num -= node_val
        if num == 0:
            self.PathArray.append(self.onePath[:])
        else:
            self.loop(tree.left, num)
            self.loop(tree.right, num)

        self.onePath.pop()
        return self.PathArray


if __name__ == '__main__':
    # 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径
    # 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径
    # https://blog.csdn.net/u010005281/article/details/79623396
    # 定义两个数组pathArray、onePath，pathArray用于存储所有符合条件的路径，onePath用于存储当前遍历的路径；
    # – 类似于深度优先搜索，每遍历到一个节点，就将其加入到onePath中，并判定是否符合条件：
    # 1. 为叶节点且和等于要求的整数，则将该数组存储至pathArray中，并换其他路径继续搜寻；
    # 2. 和小于要求的整数，则向当前节点的左右子树依次深度优先搜索；
    # 3. 和大于要求的整数，则直接换路搜索。

    so = Solution()
    node = so.build_node()
    # so.FindPath(node, 22)
    so.loop(node, 22)
    print(so.PathArray)
