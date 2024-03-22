Problem Statement:

You are given an array of integers. Write a function that finds the maximum product of two integers in the array. The function should return the maximum product and the two integers that produce it.

Input:
- An array of integers, nums, where 2 <= nums.length <= 10^5 and -10^4 <= nums[i] <= 10^4.

Output:
- A tuple (maxProduct, a, b) where maxProduct is the maximum product of two integers in the array, and a and b are the two integers that produce the maximum product.

Example:
Input: [1, 2, 3, 4, 5]
Output: (20, 4, 5)
Explanation: The maximum product is 4 * 5 = 20.
Constraints:
- The array may contain duplicate integers.
- The integers in the array can be both positive and negative.

Performance and Efficiency Requirements:
- Your solution should have a time complexity of O(n), where n is the number of integers in the array.
- Your solution should not use extra space proportional to the input size. In other words, it should not use additional arrays, maps, or sets.

Hints:
- For Golang, you can use a single pass through the array, keeping track of the maximum and second maximum integers encountered so far.
- For Node.js, you can use a similar approach, iterating over the array once and updating the maximum and second maximum integers.

Note:
- For both languages, consider edge cases like arrays with only positive or only negative integers, arrays with zeros, etc., and ensure your solution handles them correctly while maintaining efficiency.

