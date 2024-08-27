class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        LCA = root

        while LCA:
            if (p.val > LCA.val and q.val > LCA.val):
                LCA = LCA.right
            elif (p.val < LCA.val and q.val < LCA.val):
                LCA = LCA.left
            else:
                break
        return LCA


