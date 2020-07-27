"""
Problem: 1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return_list = []
        sum = 0
        for num in nums:
            sum = sum + num
            return_list.append(sum)
            
        return return_list