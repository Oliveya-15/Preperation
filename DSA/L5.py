# Palindrome Number
"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

# CODE HERE :-

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        
        r = 0
        
        while x > r:
            r = r * 10 + x % 10
            x = x // 10
        
        return x == r or x == r // 10

"""
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
