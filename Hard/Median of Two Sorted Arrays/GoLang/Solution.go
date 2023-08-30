import "sort"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	// append into one list
	res := append(nums1, nums2...)
	// sort the list
	sort.Ints(res)
	// if the total length is odd, then get the index of the median
	if len(res)%2 != 0 {
		return float64(res[len(res)/2])
	}
	// if not, get the index of median and median - 1 and divide it by 2
	return float64((res[len(res)/2] + res[len(res)/2-1])) / 2
}