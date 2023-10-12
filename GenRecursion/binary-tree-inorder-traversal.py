# https://leetcode.cn/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.

from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root: Optional[TreeNode], res: List) -> List[int]:
        if root is None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        else:
            res.extend(self.inorderTraversal(root.left))
            res.append(root.val)
            res.extend(self.inorderTraversal(root.right))
        return res

if __name__ == '__main__':
    root = [1, None, 2, 3]
    node3 = TreeNode(3)
    node2 = TreeNode(2, left=node3)
    node1 = TreeNode(1, right=node2)
    solution = Solution()
    res = solution.inorderTraversal(node1)
    print(res)
