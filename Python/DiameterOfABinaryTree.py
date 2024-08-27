class Solution(object):
    
    globalMax = 0

    def diameterOfBinaryTree(self, root):

        self.maxDepth(root)
        return self.globalMax

    def maxDepth(self,root):

        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        self.globalMax = max(self.globalMax, left+right)

        return max(left, right) +1

