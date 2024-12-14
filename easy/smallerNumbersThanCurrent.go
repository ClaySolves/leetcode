package main

func smallerNumbersThanCurrent(nums []int) []int {
	ans := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		count := 0
		for k := 0; k < len(nums); k++ {
			if i == k {
				continue
			}
			if nums[k] < nums[i] {
				count++
			}
		}
		ans[i] = count
	}

	return ans
}
