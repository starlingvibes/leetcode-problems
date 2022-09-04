"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 

Constraints:
1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(numOpen, numClose):
            if numOpen == numClose == n:
                res.append("".join(stack))
                return

            if numOpen < n:
                stack.append("(")
                backtrack(numOpen + 1, numClose)
                stack.pop()

            if numClose < numOpen:
                stack.append(")")
                backtrack(numOpen, numClose + 1)
                stack.pop()

        backtrack(0, 0)
        return res
