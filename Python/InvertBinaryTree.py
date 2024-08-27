class Solution(object):
    def invertTree(self, root):

        if root == None:
            return root

        left = root.left
        right = root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)

        return root