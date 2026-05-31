# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.kHelper(root, k)[0]

    def kHelper(self, root: Optional[TreeNode], k: int) -> tuple[int, int]:
        if root is None:
            return -1, k

        if root.left is None and root.right is None:
            return root.val, k - 1
        
        left, curr_k = self.kHelper(root.left, k)

        if curr_k == 0:
            return left, 0
        
        curr_k -= 1
        
        if curr_k == 0:
            return root.val, 0

        right, curr_k = self.kHelper(root.right, curr_k)
        
        if curr_k == 0:
            return right, 0
        
        return root.val, curr_k