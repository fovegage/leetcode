"""
题目：输入一个整数和一棵二元树。

从树的根结点开始往下访问一直到叶结点所经过的所有结点形成一条路径。

打印出和与输入整数相等的所有路径。

"""


class TreeNode:
    """
    树的节点定义，后面的很多操作都是基于节点的
    """

    def __init__(self):
        """
        定义一个树的节点，初始状态左右节点为空
        """
        self.leftNode = None
        self.rightNode = None

    def setData(self, data):
        """
        设置数字的方法
        args: data节点值
        """
        self.data = data

    def getData(self):
        """
        获取节点数字
        return:返回节点数字
        """
        return self.data

    def setLeftNode(self, leftNode):
        """
        设置左节点的方法
        args: leftNode 左节点
        """
        self.leftNode = leftNode

    def setRightNode(self, rightNode):
        """
        设置右节点的方法
        args: rightNode 右节点
        """
        self.rightNode = rightNode

    def getLeftNode(self):
        """
        获取左节点
        return:返回左节点
        """
        return self.leftNode

    def getRightNode(self):
        """
        获取右节点
        return:返回右节点
        """
        return self.rightNode


class test:
    def __init__(self):
        """
        test类的初始化，用来构造树和调用查找算法
        return:返回右节点
        """
        # self.tree = self.build_tree()
        self.index = 0
        self.data = [10, 5, 4, None, 3, None, None, 7, None, None, 12, None, None]
        self.tree = self.build_node()
        tempNode = self.tree
        data_list = []
        self.findSum(tempNode, 22, data_list)
        # print(data_list)

    def build_node(self):
        """
        根据输入，用递归的方法，构造树的方法

        https://blog.csdn.net/My_Jobs/article/details/43451187

        前序：根结点 ---> 左子树 ---> 右子树
        中序：左子树 ---> 根结点 ---> 右子树
        后序：左子树 ---> 根结点 ---> 右子树
        层次
        深度优先
        广度优先
        """
        if self.index < len(self.data):
            # 不断的取节点数据  使用前序遍历的顺序
            curr_data = self.data[self.index]
            self.index = self.index + 1
            if curr_data != None:
                # 根节点
                onNode = TreeNode()
                onNode.setData(curr_data)

                # 左
                left_node = self.build_node()
                onNode.setLeftNode(left_node)

                # 右
                right_node = self.build_node()
                onNode.setRightNode(right_node)

                # 完成一次建树
                return onNode

    def findSum(self, node, needsum, data_list):
        """
        递归调用findSum,查找和是needsum的路径
        args:
            node是树的根节点，每次递归的是节点移动
            needsum是需要求的和
            data_list里面存的是路径

        """
        if node != None and node.getData() <= needsum:
            if node.getData() < needsum:
                # 目标值 - 节点值
                newSum = needsum - node.getData()
                curr_data = node.getData()
                data_list.append(curr_data)
                self.findSum(node.getLeftNode(), newSum, data_list)
                self.findSum(node.getRightNode(), newSum, data_list)
                data_list.pop()

            else:
                # 开始打印输出路径
                if node.getData() == needsum:
                    print(data_list)
                    # for d in data_list:
                    #     print(d)
                    #     print(node.getData())
                    #     print('-----------')


if __name__ == "__main__":
    onNode = test()

    # 输出：10543-----------1057-----------1012-----------
