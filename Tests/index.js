/**
 * Function to find the maximum product of two integers in an array.
 * It iterates over the array once, keeping track of the two largest and two smallest numbers.
 * At the end, it returns the maximum product and the two numbers that produce it.
 *
 * Time complexity: O(n), where n is the number of integers in the array.
 * Space complexity: O(1), as it uses a constant amount of space.
 *
 * @param {number[]} nums - An array of integers.
 * @returns {number[]} - An array containing the maximum product and the two numbers that produce it.
 */
const main = (nums) => {
  // Define variables, initial values of maximum and minimum integers are initially as small and large as possible
  let maxInteger = -Infinity,
    penMaxInteger = -Infinity;
  let minInteger = Infinity,
    penMinInteger = Infinity;

  for (const num of nums) {
    if (num > maxInteger) {
      penMaxInteger = maxInteger;
      maxInteger = num;
    } else if (num > penMaxInteger) {
      penMaxInteger = num;
    }

    if (num < minInteger) {
      penMinInteger = minInteger;
      minInteger = num;
    } else if (num < penMinInteger) {
      penMinInteger = num;
    }
  }

  console.info(
    `Maximum integer: ${maxInteger}, Penultimate maximum integer: ${penMaxInteger}`
  );
  console.info(
    `Minimum integer: ${minInteger}, Penultimate minimum integer: ${penMinInteger}`
  );

  if (maxInteger * penMaxInteger > minInteger * penMinInteger) {
    return [maxInteger * penMaxInteger, penMaxInteger, maxInteger];
  } else {
    return [minInteger * penMinInteger, penMinInteger, minInteger];
  }
};

// ==============TEST==================
// nums = [1, 2, 3, 4, 5];
// nums = [1, 1, 2, 6, 4, -5, -6];
// nums = [2] // length of array guarateed to be >= 2 and <= 10^5
nums = [-3, -6, 0, -1, -7];
// nums = [0, 0, 0, 5, 0];
// nums = [1, 1, -3, 4, -5];
const result = main(nums);
console.log(result);

