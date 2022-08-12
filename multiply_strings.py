"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_int(x):
            strlen = len(x)
            res = 0
            for i in range(strlen - 1, -1, -1):
                res += (ord(x[i]) - 48) * 10 ** (strlen - i - 1)
            return res

        def int_to_str(y):
            numarr = []
            while True:
                numarr.append(chr(ord("0") + y % 10))
                y //= 10
                if y == 0:
                    break
            return "".join(reversed(numarr))

        num1, num2 = str_to_int(num1), str_to_int(num2)
        res = num1 * num2
        return int_to_str(res)
