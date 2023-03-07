import collections


class Solution:
    def hasPathSum(self, root, sum: int) -> bool:
        if not root:
            return False
        que_node = collections.deque([root])
        que_val = collections.deque([root.val])
        while que_node:
            now = que_node.popleft()
            temp = que_val.popleft()
            if not now.left and not now.right:
                if temp == sum:
                    return True
                continue
            if now.left:
                que_node.append(now.left)
                que_val.append(now.left.val + temp)
            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + temp)
        return False


if __name__ == '__main__':
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum = 22
    s = Solution()
    s.hasPathSum(root, targetSum)
