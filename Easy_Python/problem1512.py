#!/usr/bin/env python3

"""
Problem: 1512. Number of Good Pairs

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        jdex = 1
        count = 0

        while index < len(nums):
            while jdex < len(nums):
                if nums[index] == nums[jdex]:
                    count += 1
                jdex += 1
            index += 1
            jdex = index + 1
        
        return count

nums = [1,2,3,1,1,3]
ohohoh = Solution()
ohohoh.numIdenticalPairs(nums)