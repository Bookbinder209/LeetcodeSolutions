class Solution(object):

    def isBalanced(self, root):
        if root is None:
            return True
        
        
        left = self.isBalanced(root.left)
        if left is 0:
            return 0
        right = self.isBalanced(root.right)
        if right is 0:
            return 0

        if abs(left - right) > 1:
            return 0

        return max(left,right) +1