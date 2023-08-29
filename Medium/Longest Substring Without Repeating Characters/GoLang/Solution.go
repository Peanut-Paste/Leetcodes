// My original code
/* func lengthOfLongestSubstring(s string) int {
	if len(s) < 2 {
		return len(s)
	}
	end, res := 1, 0
	l := []string{string(s[0])}
	for end < len(s) {
		if !contains(string(s[end]), l) {
			l = append(l, string(s[end]))
			end++
		} else {
			for contains(string(s[end]), l) {
				if len(l) > 1 {
					l = append(l[:0], l[1:]...)
				} else {
					l = l[:0]
				}
			}
			l = append(l, string(s[end]))
			end++
		}
		if len(l) > res {
			res = len(l)
		}
	}
	return res
}

func contains(target string, l []string) bool {
	for _, v := range l {
		if v == target {
			return true
		}
	}
	return false
} */

// I saw some solution using hash and decided to come up my own
func lengthOfLongestSubstring(s string) int {
	// create a hash table, the character will be the
	// key, while the index of it will be the value
	m := make(map[rune]int)
	start, current, longest := 0, 0, 0
	for i, v := range s {
		// if key exist
		if idx, ok := m[v]; ok {
			// if index of existing char is higher then start
			// update start to the next index of the found
			// index
			if idx >= start {
				start = idx + 1
			}
		}
		current = i + 1 - start
		if current > longest {
			longest = current
		}
		// update hash table
		m[v] = i
	}
	return longest
}