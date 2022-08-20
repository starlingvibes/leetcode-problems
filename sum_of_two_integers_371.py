"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 
Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5
 
Constraints:
-1000 <= a, b <= 1000
"""
import math


class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = (2**a) * (2**b)
        return int(math.log2(x))
