#!/usr/bin/env python3

"""
Problem: 1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array 
are smaller than it. That is, for each nums[i] you have to count the number of 
valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        sorted_list = sorted(nums)
        return_list = []
        for num in nums:
            return_list.append(sorted_list.index(num))

        print(return_list)

        return return_list
        
ohohoh = Solution()
nums = [8,1,2,2,3]
ohohoh.smallerNumbersThanCurrent(nums)