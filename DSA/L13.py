# Sqrt(x)

"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""

# CODE HERE
class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        
        l, r = 1, x // 2
        a = 0
        
        while l <= r:
            m = (l + r) // 2
            
            if m * m == x:
                return m
            elif m * m < x:
                a = m   
                l = m + 1
            else:
                r = m - 1
        
        return a

"""
Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""