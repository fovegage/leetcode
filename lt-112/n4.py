class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.index = 0
        self.node_data = [10, 5, 4, None, 3, None, None, 7, None, None, 12, None, None]

    def build_node(self):
        current_data = self.node_data[self.index]
        self.index += 1
        if current_data != None:
            node = TreeNode(current_data)
            left = self.build_node()
            node.left = left
            right = self.build_node()
            node.right = right
            return node

    # 打印出二叉树中结点值的和为输入整数的所有路径。
    def FindPath(self, root, expectNumber):
        ans = []  # 所有路径的集合
        if root == None:
            return ans

        def iterpath(root, expectNumber, dir=[]):
            if expectNumber > root.val:
                dir.append(root.val)  # dir保存当前路径（不一定是符合要求的路径）
                # 分别在左右子树中寻找并更新期望值
                if root.left != None:
                    iterpath(root.left, expectNumber - root.val, dir)
                if root.right != None:
                    iterpath(root.right, expectNumber - root.val, dir)
            elif expectNumber == root.val:
                dir.append(root.val)
                if root.right == None and root.left == None:  # 如果节点的值与期望值相同，则判断节点是否为叶子结点，如果是叶子结点则是符合条件的路径
                    tmp = dir[:]
                    ans.append(tmp)
            else:
                dir.append(0)
            dir.pop()  # ！！！！！！！！！！！！！

        iterpath(root, expectNumber)
        return ans


if __name__ == '__main__':
    # https://www.cnblogs.com/bambipai/p/9901965.html
    data = [10, 5, 4, None, 3, None, None, 7, None, None, 12, None, None]
    num = 22
    so = Solution()
    # so.FindPath(data, num)
    node = so.build_node()
    print(so.FindPath(node, num))
    # [[10, 5, 4, 3], [10, 5, 7], [10, 12]]
