from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if root:
            q.append(root)

        res = []

        while q:
            curr_lst = []
            to_q = []

            while q:
                curr = q.popleft()
                curr_lst.append(curr.val)
                if curr.left:
                    to_q.append(curr.left)
                if curr.right:
                    to_q.append(curr.right)
            
            res.append(curr_lst)
            q.extend(to_q)

        return res

            
            