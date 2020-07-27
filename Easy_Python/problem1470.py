#!/usr/bin/env python3

"""
Problem: 1470. Shuffle the Array

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = 0
        y = n
        return_list = []
        while x < n:
            return_list.append(nums[x])
            return_list.append(nums[y])
            x += 1
            y += 1

        return return_list

nums = [2,5,1,3,4,7] 
n = 3
ohohoh = Solution()
ohohoh.shuffle(nums, n)