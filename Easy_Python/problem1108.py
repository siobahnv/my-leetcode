#!/usr/bin/env python3

"""
Problem: 1108. Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")

ohohoh = Solution()
address = "1.1.1.1"
ohohoh.defangIPaddr(address)