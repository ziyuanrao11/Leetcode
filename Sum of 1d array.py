# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:41:32 2021

@author: rao
"""
'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].'''

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length=len(nums)
        nums_new=[]
        for i in range(length):
            if i==0:
                add=nums[i]
                nums_new.append(add)
            else:
                add=nums[i]
                for j in range(i):
                    add=add+nums[j]
                nums_new.append(add)
        return nums_new

nums=[0,1,2,3,4]
s=Solution()
nums_new=s.runningSum(nums)
print(nums_new)

'''standard answer'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i + 1]) for i in range(len(nums))]

nums=[0,1,2,3,4]
s=Solution()
nums_new=s.runningSum(nums)
print(nums_new)

'''improved answer based on mine'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length=len(nums)
        nums_new=[]
        for i in range(length):
            add=sum(nums[:i+1])
            nums_new.append(add)
        return nums_new

nums=[0,1,2,3,4]
s=Solution()
nums_new=s.runningSum(nums)
print(nums_new)

'''another'''

class Solution:
    def runningSum(self, nums):
        temp_sum = 0
        for i, num in enumerate(nums):
            nums[i] += temp_sum
            temp_sum = nums[i]
        return nums
    
'''another'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
        return nums
    
'''another'''    
class Solution:
   def runningSum(self, nums):
        summ=0
        lst=[]
        for i in nums:
            summ+=i
            lst.append(summ)
        return lst

'''the best'''  
    
class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums