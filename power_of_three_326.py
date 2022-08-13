"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 
Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true
 

Constraints:
-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
"""
import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log10(n)
        y = x / math.log10(3)
        if y % 1 == 0.0:
            return True
        return False
