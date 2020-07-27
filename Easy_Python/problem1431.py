#!/usr/bin/env python3

"""
Problem: 1431. Kids With the Greatest Number of Candies

Given the array candies and the integer extraCandies, 
where candies[i] represents the number of candies that 
the ith kid has.

For each kid check if there is a way to distribute 
extraCandies among the kids such that he or she can 
have the greatest number of candies among them. Notice 
that multiple kids can have the greatest number of candies.
"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        greatest_candies = max(candies)
        list_greatest_candies = []

        for candy in candies:
            if greatest_candies > (candy + extraCandies):
                list_greatest_candies.append(False)
            else:
                list_greatest_candies.append(True)

        return list_greatest_candies

ohohoh = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
ohohoh.kidsWithCandies(candies, extraCandies)