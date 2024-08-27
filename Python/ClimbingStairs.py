class Solution(object):
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n):

        if n in self.memo:
            return self.memo[n]
        
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n < 0: 
            return 0
        
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        self.memo[n] = result
        
        return result
