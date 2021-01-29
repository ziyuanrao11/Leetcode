# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:41:20 2021

@author: rao
"""

'''You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.'''

from type import List
'''Richest Customer Wealth'''

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:   
        total = []
        for i in range (len(accounts)):
            total.append(sum(accounts[i][:]))
        return max(total)
    
'''better'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(x) for x in accounts)
    
'''simillar'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_sums = []
        for account in accounts:
            wealth_sums.append(sum(account))
        return max(wealth_sums)