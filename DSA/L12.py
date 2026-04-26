"""
Given two binary strings a and b, return their sum as a binary string.
"""

# CODE HERE

class Solution(object):
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        c = 0
        r = []

        while i >= 0 or j >= 0 or c:
            s = c

            if i >= 0:
                s += int(a[i])
                i -= 1

            if j >= 0:
                s += int(b[j])
                j -= 1

            r.append(str(s % 2))  
            c = s // 2             

        return ''.join(r[::-1])

"""
Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""