#!/usr/bin/env python3

"""
Problem: 1528. Shuffle String

Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith 
position moves to indices[i] in the shuffled string.

Return the shuffled string.
"""

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        my_tuple_list = tuple(zip(s, indices))
        my_sorted_tlist = sorted(my_tuple_list, key=lambda ml: ml[1])

        newest_list = []
        for t in my_sorted_tlist:
            newest_list.append(t[0])
        return_string = ''.join(newest_list)

        print(return_string)
        return return_string

ohohoh = Solution()
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
ohohoh.restoreString(s, indices)