"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 
Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false
 

Constraints:
1 <= num <= 2^31 - 1
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary search solution
        l, r = 0, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                return True
            else:
                if mid * mid > num:
                    r = mid - 1
                else:
                    l = mid + 1
        return False

    # Mathematical solution
        x = num ** (1/2)
        if int(x) == x:
            return True
        return False
