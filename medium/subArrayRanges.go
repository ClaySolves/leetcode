package main

import (
	"fmt"
)

func subArrayRanges(nums []int) int64 {
    n := len(nums)
    var sum int64
    
    minCache := make(map[string]int)
    maxCache := make(map[string]int)
    
    for i := 0; i < n; i++ {
        for k := i+1; k < n+1; k++ {
            if k-i < 2 { continue } 

            cacheKey := fmt.Sprintf("%d_%d", i, k)
            
            var min, max int

            if prevMin, exists := minCache[fmt.Sprintf("%d_%d", i, k-1)]; exists && k-1 > i {

                min = prevMin
                if nums[k-1] < min {
                    min = nums[k-1]
                }
            } else {
                min = nums[i]
                for j := i + 1; j < k; j++ {
                    if nums[j] < min {
                        min = nums[j]
                    }
                }
            }

            if prevMax, exists := maxCache[fmt.Sprintf("%d_%d", i, k-1)]; exists && k-1 > i {
                max = prevMax
                if nums[k-1] > max {
                    max = nums[k-1]
                }
            } else {
                max = nums[i]
                for j := i + 1; j < k; j++ {
                    if nums[j] > max {
                        max = nums[j]
                    }
                }
            }

            minCache[cacheKey] = min
            maxCache[cacheKey] = max
            
            sum += int64(max - min)
        }
    }
    return sum
}
