class Solution(object):
    def firstBadVersion(self, n):
        
        if isBadVersion(1):
            return 1
        if isBadVersion(n):
            if not isBadVersion(n-1):
                return n
        
        left = 1
        right = n
        while True:
            middle = (left+right)//2
            if isBadVersion(middle):
                if not isBadVersion(middle -1):
                    return middle
                else:
                    right = middle
            else:
                left = middle
