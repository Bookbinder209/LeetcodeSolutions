class Solution(object):
    def containsDuplicate(self, nums):

        duplicateNums = {}

        for i in nums:
            duplicateNums[i] = duplicateNums.get(i,0) +1
            if duplicateNums[i] > 1:
                return True
        
        return False
