# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        r = 0
        def traverse(root):
            if not root:
                return

            
            traverse(root.left)
            nonlocal k
            nonlocal r
            k -= 1
            if k == 0:
                r = root.val
                return
            traverse(root.right)
    
        traverse(root)
        return r
