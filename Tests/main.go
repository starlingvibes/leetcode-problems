package main

import (
	"fmt"
	"math"
)

// maxProduct takes an array of integers and returns a slice containing the maximum product of two integers in the array
// and the two integers that produce this maximum product.
// The function iterates over the array once, keeping track of the two largest and two smallest numbers.
// At the end, it returns the maximum product and the two numbers that produce it.
// Time complexity: O(n), where n is the number of integers in the array.
// Space complexity: O(1), as it uses a constant amount of space.
func maxProduct(nums []int) []int {
	  // Define variables, initial values of maximum and minimum integers are initially as small and large as possible
	maxInteger, penMaxInteger := math.MinInt64, math.MinInt64
	minInteger, penMinInteger := math.MaxInt64, math.MaxInt64

	for _, num := range nums {
		if num > maxInteger {
			penMaxInteger = maxInteger
			maxInteger = num
		} else if num > penMaxInteger {
			penMaxInteger = num
		}

		if num < minInteger {
			penMinInteger = minInteger
			minInteger = num
		} else if num < penMinInteger {
			penMinInteger = num
		}

	}

	fmt.Printf("Maximum integer: %d, Penultimate maximum integer: %d\n", maxInteger, penMaxInteger)
	fmt.Printf("Minimum integer: %d, Penultimate minimum integer: %d\n", minInteger, penMinInteger)

	if maxInteger * penMaxInteger > minInteger * penMinInteger {
		return []int{maxInteger * penMaxInteger, penMaxInteger, maxInteger}
	} else {
		return []int {minInteger * penMinInteger, penMinInteger, minInteger}
	}
}


// ==============TEST==================
func main() {
	// nums := []int{1, 1, 2, 6, 4, -5, -6}
	// nums := []int{2} // length of slice guarateed to be >= 2 and <= 10^5
	// nums := []int{0, 0, 0, 5, 0}
	nums := []int{-3, -6, 0, -1, -7}
	result := maxProduct(nums)
	fmt.Printf("%v\n", result)
}
