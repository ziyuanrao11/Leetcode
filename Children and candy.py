# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 19:52:16 2021

@author: rao
"""

'''
Given the array candies and the integer extraCandies, where candies[i] 
represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies 
among the kids such that he or she can have the greatest number of candies among them. 
Notice that multiple kids can have the greatest number of candies. '''

'''Mine'''

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        R = []
        for i in candies:
            R.append ((i+extraCandies) >= max(candies))
        return R
    
'''better'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return list(map(lambda x: True if x + extraCandies >= max(candies) 
                        else False, candies))
    
'''better'''   
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        return [i+extraCandies>=max_value for i in candies]    

