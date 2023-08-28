func twoSum(nums []int, target int) []int {
	// create a map
	m := make(map[int]int)
	// its like enumerate for loop, index and value
	for i, num := range nums {
		// idx will be the underlying value of key, if not exist then will be 0, ok is a bool to check if key exist or not
		if idx, ok := m[target-num]; ok {
			return []int{idx, i}
		}
		// create a key and value if not exist
		m[num] = i
	}
	return []int{0, 0}
}