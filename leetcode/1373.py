# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = 0
        
        def dfs(node):
            """
            Returns: (is_bst, min_val, max_val, sum)
            """
            if not node:
                return (True, float('inf'), float('-inf'), 0)
            
            # Get info from left and right subtrees
            left_is_bst, left_min, left_max, left_sum = dfs(node.left)
            right_is_bst, right_min, right_max, right_sum = dfs(node.right)
            
            # Check if current subtree is a BST
            if (left_is_bst and right_is_bst and 
                left_max < node.val < right_min):
                # Current subtree is a BST
                current_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, current_sum)
                
                # Return info about this BST
                min_val = min(left_min, node.val)
                max_val = max(right_max, node.val)
                return (True, min_val, max_val, current_sum)
                min_val = min(left_min, node.val, right_min)
                max_val = max(left_max, node.val, right_max)
                return (False, min_val, max_val, 0)
        
        dfs(root)
        return self.max_sum