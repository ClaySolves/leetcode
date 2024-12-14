package main

func countBits(n int) []int {
	sz := n + 1
	ans := make([]int, sz)
	for i := 0; i < sz; i++ {

		var count int
		store := i

		for store > 0 {
			comp := store % 2
			if comp > 0 {
				count++
			}
			store /= 2
		}

		ans[i] = count
	}

	return ans
}
