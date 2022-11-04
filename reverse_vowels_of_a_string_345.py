"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
 

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        s = list(s)
        set = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}

        for char in s:
            if char in set:
                vowels.append(char)

        for i in range(len(s)):
            if s[i] in set:
                s[i] = vowels.pop()
        return "".join(s)
