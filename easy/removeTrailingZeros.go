package main

func removeTrailingZeros(num string) string {
	iStart := 0
	for i := len(num) - 1; i >= 0; i-- {
		if num[i] == 48 {
			continue
		} else {
			iStart = i
			break
		}
	}

	var ans string = num[0 : iStart+1]

	return ans
}
