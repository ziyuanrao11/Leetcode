# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:46:14 2021

@author: rao
"""
'''most'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
    
'''faster'''
    
class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ""
        for char in address:
            if char != ".":
                defanged += char
            else:
                defanged += "[.]"
        return defanged
    
'''another'''
    
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.')) 
    
'''another'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        newStr = ""
        for letter in address:
            newStr += "[.]" if letter == "." else letter
        return newStr