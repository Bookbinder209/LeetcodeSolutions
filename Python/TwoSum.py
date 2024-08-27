class Solution(object):
    def twoSum(self, nums, target):

        dict = {}
        length = len(nums)

        for i in range(length):
            complement = target - nums[i]
            if complement in dict:
                return [dict[complement], i]
            dict[nums[i]] = i