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

def checkIfExist(arr):
    arr = sorted(arr)

    def binary_search(arr, first, last, target):
        l, r = first, last
        mid = (l + r) // 2
        while l <= r:
            if arr[mid] == target:
                return 1
            if arr[mid] > target:
                r = mid - 1
            if arr[mid] < target:
                l = mid + 1
        return 0

    for i in range(len(arr)):
        if(binary_search(arr, i + 1, len(arr) - 1, 2 * arr[i])):
            return True
    return False


# print(checkIfExist([1, 3]))
print(checkIfExist([10, 2, 5, 3]))
print(checkIfExist([7, 1, 14, 11]))
print(checkIfExist([3, 1, 7, 11]))
print(checkIfExist([-2, 0, 10, -19, 4, 6, -8]))
