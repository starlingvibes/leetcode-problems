# def largestInteger(num):
#     result = []
#     while num:
#         result.append(num % 10)
#         num //= 10

#     even_nums, odd_nums = [], []

#     def builder(result):
#         odd_nums, even_nums = [], []
#         for i in range(len(result)):
#             if result[i] % 2 == 0:
#                 even_nums.append(result[i])
#             else:
#                 odd_nums.append(result[i])
#         return odd_nums, even_nums

#     odd_nums, even_nums = builder(result)

#     odd_nums, even_nums = sorted(odd_nums), sorted(
#         even_nums)

#     res = 0
#     x = len(odd_nums + even_nums)

#     while odd_nums and even_nums:
#         if x % 2 == 1:

#         res += (odd_nums.pop() * (10 ** (x - 1)))
#         res += (even_nums.pop() * (10 ** (x - 2)))
#         x -= 2
#     if odd_nums:
#         res += odd_nums.pop()
#     elif even_nums:
#         res += even_nums.pop()

#     return res


# print(largestInteger(1234))
# print(largestInteger(65875))
# print(largestInteger(247))
# # 427

# def checkIfExist(arr):
#     arr = sorted(arr)

#     def binary_search(arr, first, last, target):
#         l, r = first, last
#         mid = (l + r) // 2
#         while l <= r:
#             if arr[mid] == target:
#                 return 1
#             if arr[mid] > target:
#                 r = mid - 1
#             if arr[mid] < target:
#                 l = mid + 1
#         return 0

#     for i in range(len(arr)):
#         if(binary_search(arr, i + 1, len(arr) - 1, 2 * arr[i])):
#             return True
#     return False


# # print(checkIfExist([1, 3]))
# print(checkIfExist([10, 2, 5, 3]))
# print(checkIfExist([7, 1, 14, 11]))
# print(checkIfExist([3, 1, 7, 11]))
# print(checkIfExist([-2, 0, 10, -19, 4, 6, -8]))

# import string
# import math


# def minimumRecolors(blocks, k):
#     ans = math.inf
#     for i in range(len(blocks) - k + 1):
#         print("i", i)
#         w = blocks[i:i + k]
#         print(w)
#         c = 0
#         for color in w:
#             if color == 'W':
#                 c += 1
#         ans = min(ans, c)
#     return ans


# print(minimumRecolors("WBBWWBBWBW", 7))
# # print(minimumRecolors("WBB", 2))


# def decode(key, message):
#     mapping = {}
#     a = list(string.ascii_lowercase)
#     count = 0
#     for char in key:
#         if char == " ":
#             continue
#         if char not in mapping:
#             mapping.update({char: a[count]})
#             count += 1
#     res = []
#     for char in message:
#         if char == " ":
#             res.append(char)
#             continue
#         res.append(mapping[char])

#     return "".join(res)


# print(decode("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
# class Solution:
# from collections import defaultdict


# def sumPrefixScores(words):
#     res = [0] * len(words)

#     # for i in range(len(words)):
#     #     res[i] = len(words[i])

#     hashmap = defaultdict(list)

#     for word in words:
#         for char in word:
#             i = 0
#             while i < len(word):
#                 i += 1
#                 if word[:i] == char:
#                     hashmap[word[:i]].append(word)

#     for i in range(len(words)):
#         for j in range(len(words[i])):
#             res[i] += len(hashmap[words[i][:j]])
#         # res[i] += len(hashmap[words[i]])

#     for i in range(len(res)):
#         res[i] += len(words[i])
#     return res


# print(sumPrefixScores(["abc", "ab", "bc", "b"]))

def sherlock(s):
    if len(set(s)) == len(s) or len(set(s)) + 1 == len(s):
        return "YES"
    else:
        return "NO"


print(sherlock("abbcc"))
